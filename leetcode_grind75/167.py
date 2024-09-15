# 167. Two Sum II

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r and numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1

        return [l+1, r+1] #1-indexed for some headass reason