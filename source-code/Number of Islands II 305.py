# 305. Number of Islands II

# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example:

# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# We return the result as an array: [1, 1, 2, 3]

# Challenge:

# Can you do it in time complexity O(k log mn), where k is the length of the positions?

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # grid = [['0' for _ in range(n)] for _ in range(m)]
        # def addLand(grid, x, y):
        #     for i in range(m):
        #         for j in range(n):
        #             if i==x and j==y:
        #                 grid[i][j] = '1'
        # def DFS(grid, x, y):
        #     if 0 <= x < m and 0<= y < n and grid[x][y]=='1':
        #         grid[x][y] = '*'
        #         DFS(grid, x-1, y)
        #         DFS(grid, x+1, y)
        #         DFS(grid, x, y-1)
        #         DFS(grid, x, y+1)
        #         grid[x][y] = '1'
        # res = []
        # rows, cols = m, n
        # for p in positions:
        #     addLand(grid, p[0], p[1])
        #     count = 0
        #     for t in range(rows):
        #         for v in range(cols):
        #             if grid[t][v] == '1':
        #                 count += 1
        #                 DFS(grid, t, v)
        #     res.append(count)
        # return res
        
        def find(i, parent):
            if i!=parent[i]:
                parent[i] = find(parent[i], parent)
            return parent[i]
        
        def union(i, j, parent):
            root1 = find(i, parent)
            root2 = find(j, parent)
            if root1 == root2:
                return True
            parent[root1] = root2
            return False
    
        res = []
        parent = [-1]*m*n
        dirs = ((0,1), (0,-1), (1,0), (-1,0))
        count = 0
        
        for pos in positions:
            idx = pos[0]*n + pos[1]
            
            parent[idx] = idx
            count +=1
            
            for d in dirs:
                i, j = pos[0] + d[0], pos[1] + d[1]
                new_idx = i*n + j
                
                if i<0 or j<0 or i>=m or j>=n or parent[new_idx]==-1:
                    continue
                    
                if not union(idx, new_idx, parent):
                    count -= 1
                    
            res.append(count)
        return res








