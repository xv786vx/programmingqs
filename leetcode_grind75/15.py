# 15. 3Sum

#my solution but really similar to ncs
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = []
        nums = sorted(nums)

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # gets rid of duplicates (checking if its == to the one before works cuz the list is sorted)
                continue

            l, r = i + 1, len(nums) - 1 # for every single i, 2 pointers l and r are used to find the other 2 numbers 
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif  nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:   
                    lst.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # means that the next number is the same as the previous one
                        l += 1 
        
        return lst

class Solution(object):
    def threeSum(self, nums):
        lst = []
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0: 
                    r -= 1
                else:
                    lst.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return lst
