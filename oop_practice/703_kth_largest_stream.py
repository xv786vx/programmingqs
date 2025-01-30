import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.lst = nums

        heapq.heapify(self.lst)

        while len(self.lst) > k:
            heapq.heappop(self.lst)


    def add(self, val: int) -> int:
        if len(self.lst) < self.k:
            heapq.heappush(self.lst, val)  # Add directly if heap is not full
        elif val > self.lst[0]:  # Only replace if num is larger than min
            heapq.heappushpop(self.lst, val)
        
        return self.lst[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)