# 63. Unique Paths II

# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # Sol 1: DP
        # dp[i][j]: num of possible unique paths
        # avoid "1" as obstacles with update 
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # time O(n*m); space O(m*n)
        # runtime: 29ms
        # --
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        
        for i in range(1, cols):
            if not obstacleGrid[0][i]:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
            else:
                obstacleGrid[0][i] = 0
        
        for i in range(1, rows):
            if not obstacleGrid[i][0]:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
            else:
                obstacleGrid[i][0] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if not obstacleGrid[i][j]:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]
        

        # sol 2: DP 1-D
        # time O(m*n); space O(n)
        # runtime: 35ms
        # --
        if not obstacleGrid: return 
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        current = [1]*cols
        current[0] = 1 - obstacleGrid[0][0]

        for i in range(1, cols): # check every col
            current[i] = current[i-1] * (1 - obstacleGrid[0][i])

        for i in range(1, rows): # check every row
            current[0] *= (1 - obstacleGrid[i][0])
            
            for j in range(1, cols):
                current[j] = (current[j-1] + current[j]) * (1 - obstacleGrid[i][j])

        return current[-1]



        


        





