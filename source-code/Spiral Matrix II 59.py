# 59. Spiral Matrix II

# Given an integer n, generate a square matrix filled with elements
#  from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # sol 1:
        # runtime: 36ms
        M = [[0] * n for _ in range(n)]
        i, j, d = 0, 0, [0, 1]
        for k in range(n*n):
            M[i][j] = k + 1
            if M[(i+d[0])%n][(j+d[1])%n]:
                d[0], d[1] = d[1], -d[0]
            i+= d[0]
            j+= d[1]
        return M
    
        # sol 2
        # runtime: 45ms
        M, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(M), lo
            M = [range(lo, hi)] + zip(*M[::-1])
        return M
                
            
            
            
            
        






