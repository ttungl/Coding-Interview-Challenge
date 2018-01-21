# 69. Sqrt(x)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # AC but not use it.
        # runtime: 75ms
        return int(math.floor(math.sqrt(x)))
        
        # sol1
        # using binary search!
        # time O(n) space O(1)
        # runtime: 52ms
        s = x
        while s**2 > x:
            s = (s+ x/s)//2
        return s
        
        # sol 2
        # using binary search
        # Time O(log n) Space O(1)
        # runtime: 72ms
        if x==0: return 0
        left, right = 1, sys.maxsize
        while left < right: # no candidate left after loop.
            mid = left + (right-left)/2
            if mid*mid > x:
                right = mid
            else:
                if (mid+1) > x/(mid+1): return mid
                left = mid + 1
        
        # sol 3:
        # Binary Search
        # Time O(log n) Space O(1)
        # runtime: 71ms
        left, right = 0, x
        while left <= right: 
            mid = left + (right - left)/2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid < x: 
                left = mid + 1
            else: 
                right = mid - 1
        

                
        