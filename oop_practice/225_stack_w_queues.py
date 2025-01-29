from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        val = self.q1.pop()
        return val

    def top(self) -> int:
        self.q2 = self.q1.copy()
        val = self.q1.pop()
        self.q1 = self.q2
        return val

    def empty(self) -> bool:
        return len(self.q1) == 0
        