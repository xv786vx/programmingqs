import math
class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        self.s2.append(val) if len(self.s2) == 0 else self.s2.append(min(self.s2[-1], val))

    def pop(self) -> None:
        self.s1.pop()
        self.s2.pop()
        
    def top(self) -> int:
        return self.s1[-1]
        
    def getMin(self) -> int:
        return self.s2[-1]
        