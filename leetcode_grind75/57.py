# 57. Insert Interval

#nc solution, work on understanding this
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            #no overlap in either condition

            else: #overlap
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])] #cleanly merges the intervals
        
        res.append(newInterval)

        return res
        