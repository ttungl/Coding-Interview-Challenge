# 252. Meeting Rooms
# ttungl@gmail.com

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        # sol 1:
        # time O(n) space O(n)
        # runtime: 65ms
        if not intervals:
            return True
        res = []
        intervals.sort(key=lambda x: x.start)
        for i in intervals:
            if res and res[-1].end > i.start:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res += i,
        return len(res) == len(intervals)
    
        # sol 2:
        # time O(n) space O(1)
        # runtime: 65ms
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        for i, j in zip(*(intervals, intervals[1:])):
            if j.start < i.end:
                return False
        return True
        
        





