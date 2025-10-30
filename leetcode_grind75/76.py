# 76 Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        res = len(s)
        min_window = (0, 0)
        t_freq, s_freq = {}, {}
        for char in t:
            t_freq[char] = 1 + t_freq.get(char, 0)
        
        l = 0
        num_matches = sum(v for v in t_freq.values())

        for r in range(0, len(s)):

            if s[r] in t:
                s_freq[s[r]] = 1 + s_freq.get(s[r], 0)

                matched = 0

                for char in s_freq.keys():
                    if s_freq[char] >= t_freq[char]:
                        matched += 1

                while matched >= len(t_freq.keys()):
                    if (r - l + 1) <= res:
                        min_window = (l, r + 1)
                        res = r - l + 1

                    if s[l] in s_freq:
                        s_freq[s[l]] -= 1
                        if s_freq[s[l]] < t_freq[s[l]]:
                            matched -= 1

                    l += 1
        
        return s[min_window[0]:min_window[1]]

