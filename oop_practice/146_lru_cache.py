class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        #left = LRU, right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next, next.prev = prev

    
    #insert right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        next.next = prev.next = node
        node.next, node.prev = next, prev
        

    def get(self, key: int) -> int:
        if self.cache.get(key):
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key]
        return -1 

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
