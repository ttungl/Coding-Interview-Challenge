# 699. Falling Squares

class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # sol 1: using dictionary.
        # find nearby positions, then find the heights of blocks based on existing and overlapping blocks.
        # update heights on left and right boundaries
        # time O(n^2) space O(n)
        # runtime: 589ms
        # --
        res, height = [], {}
        for pos, side in positions:
            left, right = pos, pos + side - 1 # find nearby positions
            adj_blocks = [key for key in height.keys() 
                            if not (key[1] < pos 
                                or key[0] > right)]
            if len(adj_blocks) >0: 
                max_h = max(height[i] for i in adj_blocks) + side
            else: 
                max_h = side
            # update height for both sides.
            height[(pos, right)] = max_h
            if len(res) == 0: 
                res.append(max_h)
            else: 
                res.append(max(res[-1], max_h))
        return res
    
        # sol 2: bisection search.
        # time: O(n log n) space O(n)
        # runtime: 72ms
        # --
        height = [0]
        pos = [0]
        max_h, res = 0, []
        for left, side in positions:
            # bisect_right() Locate the insertion point for x in a to maintain sorted order.
            # returns an insertion point which comes after (to the right of) any existing entries of item in list.
            l = bisect.bisect_right(pos, left) 
            r = bisect.bisect_left(pos, left + side)
            higher = max(height[l-1:r] or [0]) + side
            pos[l:r] = [left, left+side]
            height[l:r] = [higher, height[r-1]]
            max_h = max(max_h, higher)
            res.append(max_h)
        return res
    
        
            