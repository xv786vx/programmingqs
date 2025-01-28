class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def hash_function(self, key):
        return key % self.size    
        
    def get(self, key):
        for item in self.table[self.hash_function(key)]:
            if item.key == key:
                return item.value
        
    def set(self, key, value):
        for item in self.table[self.hash_function(key)]:
            if item.key == key:
                item.value = value
                return
    
    def remove(self, key):
        for item in self.table[self.hash_function(key)]:
            if item.key == key:
                self.table[self.hash_function(key)].remove(item)
                return
        self.table[self.hash_function(key)].pop()
        
        
    