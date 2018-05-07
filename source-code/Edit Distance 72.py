# 72. Edit Distance
# ttungl@gmail.com

# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # sol 1:
        # dynamic programming DP-2D
        # dp[i][j] = mincost of converting 
        # first i chars in w1 and j chars in w2.
        # dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][i-1]) + 1
        # time O(m*n) space O(n)
        # runtime: 264ms
        w1, w2 = len(word1)+1, len(word2)+1
        dp = [[0]*w2 for i in range(w1)]
        
        for i in range(w1): # 
        	dp[i][0] = i

        for j in range(w2): 
        	dp[0][j] = j

        for i in range(1, w1):
            for j in range(1, w2):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[-1][-1]
        
        # sol 2:
        # DP-1D
        # dp[i] = min(replace, delete, insert) + 1
        # time O(m*n) space O(n)
        # runtime: 208ms
        w1, w2 = len(word1) + 1, len(word2) + 1
        dp = [0 for i in range(w2)]
        for i in range(w2):
            dp[i] = i

        for i in range(1, w1):
            cur = [i] * w2
            for j in range(1, w2):
                cur[j] = 1 + min(cur[j-1], dp[j], dp[j-1] + (word1[i-1]!=word2[j-1]) - 1)
            dp = cur[:]
        return dp[-1]
        
        
        
