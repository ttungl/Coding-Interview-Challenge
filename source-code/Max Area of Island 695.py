# 695. Max Area of Island
# ttungl@gmail.com
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols, res = len(grid), len(grid[0]), 0
        def dfs(i, j):
            if 0<=i<rows and 0<=j<cols and grid[i][j]:
                grid[i][j]=0
                return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j+1) + dfs(i, j-1)
            return 0
        
        for i in range(rows): 
            for j in range(cols):
                res = max(res, dfs(i, j))
        return res
        
        

