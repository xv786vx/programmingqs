# 383. Ransom Note
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        h1 = {}
        for char in ransomNote:
            if char not in h1:
                h1[char] = 1
            else:
                h1[char] = h1[char] + 1
        
        for char in magazine:
            if char in h1:
                h1[char] = h1[char] - 1
        
        for char in h1:
            if h1[char] > 0:
                return False
        return True