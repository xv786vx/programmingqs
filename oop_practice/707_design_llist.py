class Node:
    def __init__(self, val):
        self.val = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        self._first = None


    def get(self, index: int) -> int:
        cur = self._first, cur_i = 0
        while cur is not None:
            if cur_i == index:
                return cur.val
            cur = cur.next
            cur_i += 1
        
        
    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self._first

        
    def addAtTail(self, val: int) -> None:
        new = Node(val)
        cur = self._first
        while cur.next is not None:
            cur = cur.next
        cur.next = new


    def addAtIndex(self, index: int, val: int) -> None:
        new = Node(val)
        if index == 0:
            new.next = self._first
            self._first = new
        else:
            cur = self._first
            cur_i = 0
            while cur is not None:
                if cur_i == index - 1:
                    cur.next = new
                    new.next = cur.next
                cur = cur.next
                cur_i += 1
            return -1             


    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self._first = self._first.next
        else:
            cur = self._first
            cur_i = 0
            while cur is not None:
                if cur_i == index - 1:
                    cur.next = cur.next.next
                cur = cur.next
                cur_i += 1
            return -1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)