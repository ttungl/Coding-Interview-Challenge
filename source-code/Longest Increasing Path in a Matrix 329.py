# 329. Longest Increasing Path in a Matrix


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # time: O(m*n)
        # space: O(m*n)
        # runtime: 392ms

        if not matrix: return 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        m = len(matrix)
        n = len(matrix[0])
        
        visited = [[-1 for _ in range(n)] for _ in range(m)]
        
        res = 0
        
        def dfs(i, j, matrix, visited, m, n):
            if visited[i][j] != -1: # return a value
                return visited[i][j]
            
            res = 1
            for d in directions:
                x, y = i + d[0], j + d[1]
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                    continue
                length = 1 + dfs(x, y, matrix, visited, m, n)
                res = max(res, length)
            visited[i][j] = res # update max
            return res
        
        
        for i in range(m):
            for j in range(n):
                clen = dfs(i, j, matrix, visited, m, n)
                res = max(res, clen)
        
        return res
        
            
            
        
        
        