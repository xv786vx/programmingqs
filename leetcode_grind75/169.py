# 169. Majority Element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hmap = {}
        for n in nums:
            if hmap.get(n):
                hmap[n] += 1
            else:
                hmap[n] = 1
        
        return max(hmap, key=hmap.get)
    