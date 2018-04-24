# 812. Largest Triangle Area
# ttungl@gmail.com
# You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation: 
# The five points are show in the figure below. The red triangle is the largest.


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # sol 1 
        # shoelace formula
        # A = 1/2 * |x1y2 + x2y3 + x3y1 - x2y1 - x3y2 -x1y3|
        # time O(n^3) space O(1)
        # runtime: 261ms
        def calcArea(x, y, z):
            return 0.5*abs(x[0]*y[1] + y[0]*z[1] + z[0]*x[1] - y[0]*x[1] - z[0]*y[1] - x[0]*z[1])
        maxA = A = i = 0
        while i < len(points):
            j = i+1 
            k = j+1
            while j < k:
                k = j+1
                while k < len(points):
                    A = calcArea(points[i], points[j], points[k])
                    maxA = max(maxA, A)
                    k += 1
                j += 1
            i += 1
        return maxA
        
        # sol 2:
        # time O(n^3)
        # runtime: 186ms
        def calcArea(x,y,z):
            return 0.5*abs(x[0]*y[1] + y[0]*z[1] + z[0]*x[1] - y[0]*x[1] - z[0]*y[1] - x[0]*z[1])
        return max(calcArea(i,j,k) for i,j,k in itertools.combinations(points, 3))
        
        
        