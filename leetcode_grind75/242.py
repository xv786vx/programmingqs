class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        for c in s:
            if c not in hmap:
                hmap[c] = 1
            else:
                hmap[c] = hmap[c] + 1 

        for c in t:
            if c in hmap:
                hmap[c] = hmap[c] - 1
            else:
                return False

        for c in hmap:
            if hmap[c] != 0:
                return False
        return True



    

