# 63. Unique Paths II

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # Sol 1: DP
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

        for i in range(1, cols):
            current[i] = current[i-1] * (1 - obstacleGrid[0][i])

        for i in range(1, rows):
            current[0] *= (1 - obstacleGrid[i][0])
            for j in range(1, cols):
                current[j] = (current[j-1] + current[j]) * (1 - obstacleGrid[i][j])

        return current[-1]



        


        





