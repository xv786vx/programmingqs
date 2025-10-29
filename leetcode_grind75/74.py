# 74 Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1
        
        row = (top + bot) // 2

        low, high = 0, len(matrix[row]) - 1
        while low <= high:
            mid = (low + high) // 2
            if target < matrix[row][mid]:
                high = mid - 1
            elif target > matrix[row][mid]:
                low = mid + 1
            else:
                return True
        
        return False

            