class MyHashSet:

    def __init__(self):
        self.table = []
    
    def hash_function(self, key):
        return key % self.size
        

    def add(self, key: int) -> None:
        for item in self.table:
            if item == key:
                return
        self.table.append(key)
        return
        

    def remove(self, key: int) -> None:
        for item in self.table:
            if item == key:
                self.table.remove(item)
                return
        

    def contains(self, key: int) -> bool:
        for item in self.table:
            if item == key:
                return True
        return False