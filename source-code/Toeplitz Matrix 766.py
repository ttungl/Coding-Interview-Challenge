# 766. Toeplitz Matrix

# A matrix is Toeplitz if every diagonal 
# from top-left to bottom-right has the same element.

# Now given an M x N matrix, return True if and only if 
# the matrix is Toeplitz.

# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: True
# Explanation:
# 1234
# 5123
# 9512

# In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", 
# "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are 
# the same, so the answer is True.

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # sol 1
        # DFS
        # time O(n^2) space O(1)
        # runtime: 54ms
        rows, cols = len(matrix), len(matrix[0])
        def dfs(i, j): # check diagonal
            pixel = matrix[i][j]
            while 0<= i < rows and 0<=j<cols:
                if matrix[i][j]==pixel: 
                    i+=1; j+=1
                else:
                    return False
            return True
        for i in range(rows): # rows
            if not dfs(i, 0): return False
        [False if not dfs(0, i) else True for i in range(cols)] # cols
        return True
                
                
        # sol 2
        # time O(n^2) space O(1)
        # runtime: 56ms
        rows, cols = len(matrix), len(matrix[0])
        return all([False if matrix[i][j] != matrix[i+1][j+1] else True for i in range(rows-1) for j in range(cols-1)])
    
        
        
        
                    
        