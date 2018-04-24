# 54. Spiral Matrix
# ttungl@gmail.com
# Given a matrix of m x n elements (m rows, n columns), 
# return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # sol 1:
        # time O(n^2) space O(n)
        # runtime: 30ms
        res = []
        if len(matrix)==0: return res
        rowBegin = 0
        rowEnd = len(matrix)-1
        colBegin = 0
        colEnd = len(matrix[0])-1 
        while (rowBegin <= rowEnd and colBegin <= colEnd):
            # right
            for j in range(colBegin, colEnd+1):
                res.append(matrix[colBegin][j])
            rowBegin+=1
            # down
            for j in range(rowBegin, rowEnd+1):
                res.append(matrix[j][colEnd])
            colEnd-=1
            # left
            if rowBegin <= rowEnd:
                for j in range(colEnd, colBegin-1, -1):
                    res.append(matrix[rowEnd][j])
            rowEnd-=1
            # up
            if colBegin <= colEnd:
                for j in range(rowEnd, rowBegin-1, -1):
                    res.append(matrix[j][colBegin])
            colBegin+=1
        return res
    
        # sol 2
        # runtime: 31ms
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
    
        # sol 3:
        # runtime: 32ms
        res = []
        while matrix:
            res += matrix.pop(0) # res=[1 2 3] + [6 9] + [8 7] + [4 5]
            matrix = zip(*matrix) # matrix=[[4 7],[5 8],[6 9]];[[5 4] [8 7]]; [[5 4]]
            matrix.reverse() # matrix = [[6 9], [5 8], [4 7]]; [[8 7], [5 4]]; [[4 5]]; [[]]
        return res
        
        # sol 4:
        # runtime: 28ms
        res = []
        while matrix:
            res +=matrix.pop(0)
            matrix = zip(*matrix)[::-1] # asterisk to unpack a list of list.
        return res

        
        
        
        