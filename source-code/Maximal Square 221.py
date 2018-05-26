# 221. Maximal Square
# ttungl@gmail.com

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# For example, given the following matrix:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # sol 1:
        # Use dynamic programming 1-D
        # Keep maintaining the previous state [i-1]. 
        # Maintain max res.
        # time O(n^2) space O(n)
        # runtime: 145ms
        if not matrix: 
            return 0
        res = last_elem = 0
        rows, cols = len(matrix), len(matrix[0])
        
        dp = [0]*(cols+1)

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                tem = dp[j] # maintain last element
                if matrix[i-1][j-1]=='0': 
                    dp[j] = 0
                else:
                    dp[j] = min(min(dp[j], dp[j-1]), last_elem) + 1
                    res = max(res, dp[j])
                last_elem = tem
        return res*res # square area
    
        