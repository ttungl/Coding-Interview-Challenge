# 518. Coin Change 2
# ttungl@gmail.com

# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

# Note: You can assume that

# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
# Example 1:

# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:

# Input: amount = 10, coins = [10] 
# Output: 1

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # sol 1:
        # dp[i] is the number of combinations of the coins to make up the amount.
        # for each coin, try all from the amount, if the current amount >= current coin,
        # update the dp[i-c] to dp[i]
        # time O(n*m) space O(n)
        # runtime: 230ms
        dp = [1] + [0]*amount
        for c in coins:
            for i in range(1, amount + 1):
                if c <= i:
                    dp[i] += dp[i-c]
        return dp[-1]
    
        # sol 2:
        # knapsack problem
        # + When not using the i-th coin, only using the first (i-1) coins to make up amount j, 
        # so we have dp[i-1][j] ways.
        # + When using the i-th coin, since we can use unlimited same coin, 
        # we need to know all combinations to make up amount (j - coins[i]) 
        # by using first i coins (including ith), which is dp[i][j-coins[i]]
        # Init: dp[i][0] = 1
        # runtime: 881ms
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        for i in range(1, len(coins) + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]
                dp[i][j] += dp[i-1][j]
        return dp[-1][-1]
        
        
    
        
            

