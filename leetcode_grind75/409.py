# 409. Longest Palindrome

#redo this today
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = {}
        count = 0
        for c in s:
            if c not in hmap:
                hmap[c] = 1
            else:
                hmap[c] += 1
                if hmap[c] % 2 == 0:
                    count += 2
        return count + 1 if len(s) - count != 0 else count