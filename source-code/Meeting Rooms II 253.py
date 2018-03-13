# 253. Meeting Rooms II

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # sol 1:
        # using priority queue (minheap)
        # runtime: 62ms
        res = []
        intervals.sort(key=lambda x: x.start)
        for i in intervals:
            if res and res[0] <= i.start:
                # intervals share the same room
                heapq.heapreplace(res, i.end)
            else:
                heapq.heappush(res, i.end) # add a new room
        return len(res)
    
    
        # sol 2:
        # runtime: 70ms
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        a = numroom = e = 0
        for s in starts:
            while ends[e] <= s: # check meeting ends
                a += 1
                e += 1
            if a > 0: # if room's available
                a -= 1
            else: # add new room
                numroom += 1
        return numroom
            
            
