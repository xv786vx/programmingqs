#3. Longest Substring Without Repeating Characters

#might actually keep myself safe
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, cset, max_length = 0, set(), 0
        for r in range(0, len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[r])

            max_length = max(max_length, r - l + 1)
        
        return max_length