import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
        
        # left = LRU, right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

        # Initialize the plot
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("LRU Cache Visualization")
        self.ax.set_xlim(0, self.capacity + 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_xticks([])
        self.ax.set_yticks([])

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        nxt.prev = prev.next = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.visualize()
            return self.cache[key].val
        self.visualize()
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        self.visualize()

    def visualize(self):
        self.ax.clear()  # Clear the previous plot
        self.ax.set_title("LRU Cache Visualization")
        self.ax.set_xlim(0, self.capacity + 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        current = self.left.next
        x = 1
        while current != self.right:
            # Draw the node
            self.ax.text(x, 0.5, f'{current.key}:{current.val}', fontsize=12, ha='center', va='center', 
                         bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.5'))
            
            # Draw the next pointer (arrow to the right)
            if current.next != self.right:
                self.ax.arrow(x + 0.3, 0.5, 0.4, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')
            
            # Draw the prev pointer (arrow to the left)
            if current.prev != self.left:
                self.ax.arrow(x - 0.3, 0.5, -0.4, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')
            
            current = current.next
            x += 1

        plt.draw()
        plt.pause(0.1)  # Pause to allow the plot to update

# Initialize the LRUCache with a given capacity
capacity = int(input("Enter the capacity of the LRU Cache: "))
lru_cache = LRUCache(capacity)

# Command loop
while True:
    command = input("Enter a command (put <key> <value>, get <key>, or exit): ").strip().split()
    if not command:
        continue

    if command[0] == "put" and len(command) == 3:
        try:
            key = int(command[1])
            value = int(command[2])
            lru_cache.put(key, value)
        except ValueError:
            print("Invalid input. Key and value must be integers.")
    elif command[0] == "get" and len(command) == 2:
        try:
            key = int(command[1])
            result = lru_cache.get(key)
            print(f"Value for key {key}: {result}")
        except ValueError:
            print("Invalid input. Key must be an integer.")
    elif command[0] == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid command. Use 'put <key> <value>', 'get <key>', or 'exit'.")

# Keep the window open
plt.ioff()
plt.show()