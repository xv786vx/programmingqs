# 278. First Bad Version

#solution from yt
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower, upper, result = 1, n, n
        while lower <= upper:
            middle = (lower + upper) // 2
            if isBadVersion(middle):
                result = middle
                upper = middle-1
            else:
                lower = middle+1
        
        return result

#recursion w chat (write this out again)
class Solution(object):
    def firstBadVersion(self, n):
        def helper(left, right):
            if left == right:
                return left
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                return helper(left, mid)
            else:
                return helper(mid + 1, right)

        return helper(1, n)