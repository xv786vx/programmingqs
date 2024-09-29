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
            if newInterval[1] < intervals[i][0]: #if end of new interval is less than start of current interval
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]: #if start of new interval is greater than end of current interval
                res.append(intervals[i])
            
            #no overlap in either condition

            else: #overlap
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])] #cleanly merges the intervals
        
        res.append(newInterval)

        return res
        