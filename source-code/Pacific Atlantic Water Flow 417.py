# 417. Pacific Atlantic Water Flow 

# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:

# Given the following 5x5 matrix:

#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # sol 1:
        # runtime: 179ms
        def findBorder(border):
            queue = collections.deque(border)
            while queue:
                (i,j) = queue.popleft()
                for d in ((-1,0),(1,0),(0,-1),(0,1)):
                    x, y = i+d[0], j+d[1]
                    if 0<= x< m and 0<=y<n and (x,y) not in border and matrix[x][y] >= matrix[i][j]:
                        queue.append((x,y))
                        border.add((x,y))
            return border
        if not matrix: 
            return []
        m, n = len(matrix), len(matrix[0])
        pacific = set([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)])
        atlantic = set([(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n-1)])
        return list(findBorder(pacific) & findBorder(atlantic))
        

        # sol 2:
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
    
        
            