# 827. Making A Large Island

# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

# After, what is the size of the largest island? (An island is 
# a 4-directionally connected group of 1s).

# Example 1:

# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, 
# then we get an island with area = 3.

# Example 2:

# Input: [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, 
# only one island with area = 1.
# Example 3:

# Input: [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 1.
 

# Notes:

# 1 <= grid.length = grid[0].length <= 50.
# 0 <= grid[i][j] <= 1.


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # sol 1:
        # move() and dfs()
        # move(): return all possible next positions in 4-dir.
        # dfs(): check every island one-cell, count its area.
        # for every island one-cell, map its index (init=2) to area.
        # check every zero-cell, maintain maxArea.
        # runtime: 124ms
        
        directions = ((-1,0), (0,-1), (1,0), (0,1))
        rows, cols = len(grid), len(grid[0])
        
        # return all possible next positions in 4-dir.
        def move(x, y):
            for i, j in directions:
                a, b = x+i, y+j
                if 0 <= a < rows and 0 <= b < cols:
                    yield a, b
            
        # check every island, count its area.
        def dfs(x, y, idx):
            a = 0
            grid[x][y] = idx
            for i, j in move(x, y):
                if grid[i][j]==1:
                    a += dfs(i, j, idx)
            return a+1
            
        # every island, map its index to area.
        area = collections.defaultdict(int)
        idx = 2
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area[idx] = dfs(i, j, idx)
                    idx += 1
        
        # check every zero-cell, maintain maxArea.
        res = max(area.values() or [0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    check = set(grid[x][y] for x, y in move(i, j) if grid[x][y] > 1)
                    res = max(res, sum(area[idx] for idx in check) + 1)
        return res
        
        
                    









