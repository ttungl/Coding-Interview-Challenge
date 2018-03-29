# 64. Minimum Path Sum

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # sol 1:
        # Dynamic Programming
        # find dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        # runtime: 70ms
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0] # init
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
        
        
        # sol 2:
        # Dynamic Programming 2D
        # runtime: 66ms
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j-1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
                
        # sol 3:
        # DP-1D
        # runtime: 52ms
        dp = [0]*len(grid[0])
        dp[0] = grid[0][0]
        for i in range(1, len(grid[0])):
            dp[i] = dp[i-1] + grid[0][i]
        for i in range(1, len(grid)):
            dp[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]

        
                
                
                
            
            
        
                
                
                
            
            
        






