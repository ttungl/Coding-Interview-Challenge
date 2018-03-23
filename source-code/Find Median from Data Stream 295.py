# 295. Find Median from Data Stream


# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# Examples: 
# [2,3,4] , the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2

from heapq import *

class MedianFinder(object):
    
    # sol 1
    # priority queue
    # time O(log n) space O(n)
    # runtime: 605ms
    def __init__(self):
        """
        initialize your data structure here.
        """
        # max (lo) and min (hi) heaps
        # lo: stores a smaller half
        # hi: stores a larger half
        # find median will takes O(1).
        self.heaps = [], [] 

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        lo, hi = self.heaps
        heappush(lo, -heappushpop(hi, num))
        if len(hi) < len(lo):
            heappush(hi, -heappop(lo))
        

    def findMedian(self):
        """
        :rtype: float
        """
        lo, hi = self.heaps
        if len(hi) <= len(lo):
            return (hi[0] - lo[0])/2.0
        return float(hi[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()