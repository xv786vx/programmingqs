# 49 Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            s_arr = ''.join(sorted(list(s)))
            if anagrams.get(s_arr) is None:
                anagrams[s_arr] = [s]
            else:
                anagrams[s_arr].append(s)
        
        res = []
        for key in anagrams.keys():
            res.append(anagrams[key])
        
        return res
