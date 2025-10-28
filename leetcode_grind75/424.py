# 424 Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res, hmap = 0, 0, {}
        for r in range(0, len(s)):
            if hmap.get(s[r]) is None:
                hmap[s[r]] = 1
            else:
                hmap[s[r]] += 1
            maxCount = max(v for v in hmap.values())

            while (r - l + 1) - maxCount > k:
                hmap[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))
        
        return res
