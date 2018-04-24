# 463. Island Perimeter
# ttungl@gmail.com

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # sol 1:
        # runtime: 322ms
        # --
        rows, cols, res = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    res+=4
                    if j>0 and grid[i][j-1]==1: res-=1
                    if j<cols-1 and grid[i][j+1]==1: res-=1
                    if i>0 and grid[i-1][j]==1: res-=1
                    if i<rows-1 and grid[i+1][j]==1: res-=1
        return res
    
    
        # sol 2
        # runtime: 259ms
        # --
        rows, cols, res = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    res+=4
                    if i-1>=0 and grid[i-1][j]==1: res-=2
                    if j-1>=0 and grid[i][j-1]==1: res-=2
        return res
        
            



