# 498. Diagonal Traverse

# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:

# Note:
# The total number of elements of the given matrix will not exceed 10,000.


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # sol 1:
        # nums on a diagonal line have the same sum of i and j.
        # time O(n^2) space O(n)
        # runtime: 240ms
        res = []
        if not matrix:
            return res
        rows, cols = len(matrix), len(matrix[0])
        dict = collections.defaultdict(list)
        
        for i in range(rows):
            for j in range(cols):
                dict[i+j+1].append(matrix[i][j])

        for k, d in dict.iteritems():
            if k % 2 == 1:
                res += d[::-1]
            else:
                res += d
        return res
    
        
            
            
        
