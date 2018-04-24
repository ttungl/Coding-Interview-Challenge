# 774. Minimize Max Distance to Gas Station
# ttungl@gmail.com
# On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

# Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

# Return the smallest possible value of D.

# Example:

# Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
# Output: 0.500000
# Note:

# stations.length will be an integer in range [10, 2000].
# stations[i] will be an integer in range [0, 10^8].
# K will be an integer in range [1, 10^6].
# Answers within 10^-6 of the true value will be accepted as correct.
# Discuss




class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        # sol 1: 
        # use binary search to find the smallest possible D.
        # lo, hi= distance btw first and last station
        # count = # gas station that makes it possible.
        # if count > K, then mid is too small if K is added.
        # if count < K, then mid is possible and continue to find a max one.
        # when lo+1e-6 < hi, then the answer within 10e-6 of the true value.
        # runtime 1491ms
        bound, s = 1e-6, stations
        lo, hi = bound, s[-1]-s[0]
        while lo + bound < hi:
            mid = lo + (hi-lo)/2
            count = 0
            for v1,v2 in zip(s, s[1:]): 
                count += max(0, math.ceil((v2 - v1)/mid) - 1) 
            if count > K: lo = mid
            else: hi = mid
        return hi


        # sol 2: 
        # priority queue
        # time O(n log n) space O(n)
        # runtime: 315ms
        s = stations
        d, heap = (s[-1]-s[0])/float(K), [] # minmax distance is no more than (station(n-1)-station(0)) / K
        for v1, v2 in zip(s, s[1:]):
            x = max(1, int((v2-v1)/d)) 
            K-= x-1
            heapq.heappush(heap, (float(v1-v2)/x, v1, v2, x))
        for i in range(K):
            (d, x, y, j) = heap[0] # pop
            heapq.heapreplace(heap, ((x-y)/(j+1.0), x, y, j+1))
        return -heap[0][0]




        
        
        
        
        

