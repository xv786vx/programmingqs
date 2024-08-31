# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeBrackets = {")" : "(", "}" : "{", "]" : "["}
        for bracket in s:
            if bracket in closeBrackets:
                if stack and stack[-1] == closeBrackets[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False