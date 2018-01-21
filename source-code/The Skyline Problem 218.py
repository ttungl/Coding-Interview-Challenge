# 218. The Skyline Problem

# clear explanation: https://briangordon.github.io/2014/08/the-skyline-problem.html

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # sol 1: mergesort
        # when merging, maintain the max height.
        #   if left part, update height 1, otherwise, right part, update height 2. 
        # runtime: 155ms
        # time O(n log n); space O(n)
        # --
        def merge(left, right):
            h1, h2, res = 0, 0, []
            while left and right:
                if left[0][0] < right[0][0]:
                    pos, h1 = left[0] # update left edge position and its height.
                    left = left[1:] # update left
                elif left[0][0] > right[0][0]:
                    pos, h2 = right[0] # update right edge and height
                    right = right[1:] # update right
                else:
                    # position and height of left, and height of right.
                    pos, h1 = left[0] 
                    h2 = right[0][1] 
                    left = left[1:] # update left and right
                    right = right[1:]
                # update max height.
                max_h = max(h1, h2) 
                # append position and height.
                if not res or max_h != res[-1][1]: # res[-1][1]: last height
                    res.append([pos, max_h])
            # update res on left and right.
            if left: res += left
            if right: res += right
            return res
        # main
        if not buildings: 
            return []
        if len(buildings)==1: 
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = len(buildings)//2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return merge(left, right)
    
    
        # sol 2: priority queue (maxheap)
        # Use an infinite vertical line x to scan from left to right. If max height changes, record [x, height] in res.
        # runtime: 92ms
        # time O(n log n); space O(n)
        # --
        skylines = sorted([(left, -height, right) for left, right, height in buildings] + list({(right, 0, None) for _, right, _ in buildings})) # set comprehension
        res, hx = [[0,0]],[(0,float("inf"))] 
        for x, nHeight, pright in skylines: 
            while x >= hx[0][1]: # pop heap if current height changes greater than or equal to max height of heap.
                heapq.heappop(hx)
            if nHeight < 0: # add to the heap all positions [L, R] in [L, -H, R].
                heapq.heappush(hx, (nHeight, pright))
            if res[-1][1] + hx[0][0]: 
                res += [x, -hx[0][0]],
        return res[1:]
            
        
        
    
        
 