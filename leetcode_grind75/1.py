# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index, number in enumerate(nums):
            if target - number in hmap:
                return[hmap[target - number], index]
            hmap[number] = index
        