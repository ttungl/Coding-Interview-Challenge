# 56. Merge Intervals 


# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # sol 1:
        # runtime: 82ms
        if not intervals: 
            return []
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prev, cur  = res[-1], intervals[i]
            if cur.start <= prev.end: # merge
                prev.end = max(prev.end, cur.end)
            else:
                res.append(cur)
        return res
        
        # sol 2:
        # runtime: 83ms
        res = []
        for i in sorted(intervals, key=lambda x: x.start):
            if res and res[-1].end >= i.start: # merge
                res[-1].end = max(res[-1].end, i.end)
            else:
                res += i,
        return res
            
            
                
        

