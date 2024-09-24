# 347. Top K Frequent Elements

#first medium by myself yippee
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hmap = {}
        for n in nums:
            if hmap.get(n):
                hmap[n] += 1 
            else:
                hmap[n] = 1
        
        arr = []
        for i in hmap:
            arr.append([-hmap[i], i])

        heapq.heapify(arr)

        res = []
        while k != 0:
            freq, num = heapq.heappop(arr)
            res.append(num)
            k -= 1 

        return res