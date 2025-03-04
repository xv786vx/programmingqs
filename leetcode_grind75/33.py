# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        # find k
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] <= nums[end]:
                end = mid
        k = start
        print(k)

        if k == 0:
            start, end = 0, len(nums) - 1
        else:
            if target >= nums[0]:
                start, end = 0, k - 1
            else:
                start, end = k, len(nums) - 1
        
        def bs(arr, start, end, target):
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        return bs(nums, start, end, target)


        