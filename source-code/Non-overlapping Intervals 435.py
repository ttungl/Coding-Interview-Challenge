# 435. Non-overlapping Intervals

# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note:
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
# Example 1:
# Input: [ [1,2], [2,3], [3,4], [1,3] ]

# Output: 1

# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:
# Input: [ [1,2], [1,2], [1,2] ]

# Output: 2

# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:
# Input: [ [1,2], [2,3] ]

# Output: 0

# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # sol 1:
        # time O(n log n) space O(n)
        # runtime: 53ms
        res, minIntervals = [], 0
        intervals.sort(key=lambda x: x.end)
        for i in intervals:
            if res and res[-1].end > i.start:
                minIntervals += 1
            else:
                res += i,
        return minIntervals
    
    
        # sol 2:
        # time O(n log n) space O(1)
        # runtime: 56ms
        intervals.sort(key=lambda x: x.end)
        prev = minIntervals = 0    
        for i in range(1, len(intervals)):
            if intervals[prev].end > intervals[i].start:
                minIntervals += 1
                prev = i if intervals[prev].end > intervals[i].end else prev
            else:
                prev = i
        return minIntervals 
    
        
        











