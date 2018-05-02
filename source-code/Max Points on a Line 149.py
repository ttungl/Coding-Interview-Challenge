# 149. Max Points on a Line
# ttungl@gmail.com

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # sol 1:
        # use dict to keep track of slops increasing.
        # max of d[slop] and then max of res vs. curmax+overlap+1.
        # overlap is when dx=dy=0.
        # runtime:
        if len(points) <= 2: 
            return len(points)
        
        res, d = 0, collections.defaultdict(int)

        def findGCD(x, y):
            if y==0: return x
            return findGCD(y, x % y)

        for i in range(len(points)):
            d.clear()
            curmax = overlap = 0
            for j in range(i + 1, len(points)):

                dx, dy = points[j].x - points[i].x, points[j].y - points[i].y
                if dx == dy == 0:
                    overlap += 1
                    continue
                
                gcd = findGCD(dx, dy) # gcd-> slope.
                dx, dy = dx/gcd, dy/gcd
                
                d[(dx, dy)] += 1
                curmax = max(curmax, d[(dx, dy)])
            res = max(res, curmax + overlap + 1)
        return res
        
        
        


