# 780. Reaching Points
# ttungl@gmail.com
# A move consists of taking a point (x, y) and transforming it to either
# (x, x+y) or (x+y, y).

# Given a starting point (sx, sy) and a target point (tx, ty), 
# return True if and only if a sequence of moves exists to transform
# the point (sx, sy) to (tx, ty). Otherwise, return False.

# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)

# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False

# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True

# Note: sx, sy, tx, ty will all be integers in the range [1, 10^9].

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        # sol 1:
        # runtime: 34ms
        while tx > 0 and ty > 0 and tx != ty and (tx > sx or ty > sy):
            if tx > ty:
                k = (tx - sx) // ty
                tx -= k*ty
            else:
                k = (ty - sy) // tx
                ty -= k*tx
            if k < 1:
                return False
        if tx == sx and ty == sy:
            return True
        if tx == ty and ((sx == 0 and sy == tx) or (sy == 0 and sx == tx)):
            return True
        return False
    
        # sol 2
        # runtime: 34ms
        while (sx<tx or sy<ty) and tx!=ty:
            if tx < ty:
                ty -= (max(((ty-sy)//tx), 1))*tx
            else:
                tx -= (max(((tx-sx)//ty), 1))*ty
        return (sx==tx and sy==ty)
                
        # sol 3
        # reduce tx,ty if they're greater than starting points.
        # check (x, y+kx) or (x+ky, y)
        # time O(n) space O(1)
        # runtime: 34ms
        while sx < tx and sy < ty:
            tx, ty = tx%ty, ty%tx
            
        return (sx==tx and (ty-sy)%sx==0) or (sy==ty and (tx-sx)%sy==0)
    
    
        
    
    
    
    
        
    
    