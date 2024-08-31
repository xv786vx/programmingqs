# 125. Valid Pailndrome

#submission 1
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(" ", "").lower()
        punc = '''!()`-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in s:
            if char in punc:
                s = s.replace(char, "")

        i = 0
        j = len(s)-1

        while i != j and j>0 and i<len(s)-1:
            if s[i] == s[j]: 
                i = i+1
                j = j-1
            else:
                return False
        return True