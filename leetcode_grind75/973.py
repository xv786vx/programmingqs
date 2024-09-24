#973. K Closest Points to Origin

#nc ahh solution 
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minheap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2) 
            minheap.append([dist, x, y])
        
        heapq.heapify(minheap) #starting from the right-most leaf node, heapify the tree (reference notes for how this happens exactly), pushing the smallest element to the top
        res = []
        while k != 0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1
        
        return res