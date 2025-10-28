# 567 Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_h, s2_h = {}, {}
        for i in range(len(s1)):
            s1_h[s1[i]] = 1 + s1_h.get(s1[i], 0)
            s2_h[s2[i]] = 1 + s2_h.get(s2[i], 0)

        if s1_h == s2_h:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            s2_h[s2[r]] = 1 + s2_h.get(s2[r], 0)
            s2_h[s2[l]] -= 1

            if s2_h[s2[l]] == 0:
                del s2_h[s2[l]]
            
            l += 1

            if s1_h == s2_h:
                return True
        
        return False
