# 417. Pacific Atlantic Water Flow 

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # time: O(n * m)
        # space: O(n * m)
        # runtime: 222ms

        # corner case
        if not matrix: return []
        
        m = len(matrix) # rows
        n = len(matrix[0]) # cols
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        res = []
        
        # explore neighbors of a node/point
        def dfs(i, j, matrix, visited, m, n):
            visited[i][j] = True # visited point (i,j) 
            for d in directions:
                x, y = i + d[0], j + d[1]
                if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]: 
                    continue
                dfs(x, y, matrix, visited, m, n)
        
        # rows
        for i in range(m):
            dfs(i, 0, matrix, p_visited, m, n)
            dfs(i, n-1, matrix, a_visited, m, n)
        
        # cols
        for j in range(n):
            dfs(0, j, matrix, p_visited, m, n)
            dfs(m-1, j, matrix, a_visited, m, n)
        
        # check visited matrices
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])
        
        return res
    
        
            