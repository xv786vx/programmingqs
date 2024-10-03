# 485. Max Consecutive Ones

#my solution
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consec = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                consec += 1 
            else:
                consec = 0
                
            res = max(consec, res)
        return res