# 73. Set Matrix Zeroes


# Given a m x n matrix, if an element is 0, set its entire row and 
# column to 0. Do it in place with space O(1).

# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # sol 1:
        # time O(n^2) space O(n)
        # runtime: 201ms
        rows, cols = len(matrix), len(matrix[0])
        def zerosRowCol(i, j, visited): # i=row, j=col
            row = col = 0
            while row < rows:
                if (row, j) not in visited:
                    if matrix[row][j] !=0:
                        matrix[row][j] = 0
                        visited.add((row, j))
                row+=1
            while col < cols:
                if (i, col) not in visited:
                    if matrix[i][col] !=0:
                        matrix[i][col] = 0
                        visited.add((i, col))
                col+=1
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0 and ((i,j) not in visited):
                    visited.add((i, j))
                    zerosRowCol(i, j, visited)
        
        # sol 1 updated
        # runtime: 189ms
        def cleaningRC(matrix, i, j):
            for r in range(len(matrix)):
                if (r,j) not in visited and matrix[r][j]!=0:
                    matrix[r][j] = 0
                    visited.add((r,j))
            for c in range(len(matrix[0])):
                if (i,c) not in visited and matrix[i][c]!=0:
                    matrix[i][c] = 0
                    visited.add((i,c))
                
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and (i,j) not in visited:
                    visited.add((i,j))
                    cleaningRC(matrix, i, j)
                    
    
        # sol 2
        # time O(n^2) space O(m*n)
        # runtime: 153ms
        rowset = []; colset = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    rowset.append(i)
                    colset.append(j)
        for i in range(len(matrix)):
            if i in rowset:
                for j in range(len(matrix[i])):
                    matrix[i][j]=0
        for j in range(len(matrix[0])):   
            if j in colset:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
                    
                    
        # sol 3:
        # bit manipulation
        # runtime: 162ms
        row = col = 0
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row |= 1<<i
                    col |= 1<<j
        for i in range(rows):
            for j in range(cols):
                if row&(1<<i) | col&(1<<j):
                    matrix[i][j] = 0










                    
        
                    