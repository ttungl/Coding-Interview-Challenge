# 322. Coin Change
# ttungl@gmail.com
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)

# Example 2:
# coins = [2], amount = 3
# return -1.

# Note:
# You may assume that you have an infinite number of each kind of coin.


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # sol 1:
        # use Dynamic Programming
        # Assume dp[i] is the fewest number of coins making up the amount i.
        # For every coin in coins, dp[i] = min(dp[i - coin]) + 1.
        # runtime: 1212ms
        dp = [0] + [float('Inf')] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >=0 else float('Inf') for c in coins]) + 1
        return [dp[-1], -1][dp[-1]==float('Inf')]
        
        
        # sol 2:
        # Dynamic Programming
        # dp[i] is the fewest number of coins making up the amount.
        # if (i - coin) >= 0 and dp[i-c] != -1, there's a solution where dp[i] = min(dp[i-c]) + 1
        # runtime: 1328ms
        dp = [0] + [-1]*amount
        for c in coins:
            for i in range(1, amount + 1):
                if i - c >= 0 and dp[i - c]!= -1:
                    dp[i] = min(dp[i], dp[i-c] + 1) if dp[i] > 0 else (dp[i-c] + 1)
        return dp[-1]
        
        # sol 3:
        # using DFS recursive.
        # three arguments in DFS method include index, amount, and count.
        # index is the index of the range (start, length of number of coins).
        # count is to keep track of number of coins.
        # runtime: 328ms
        def dfs(index, amount, count):
            if amount == 0:
                self.res = min(self.res, count)
            for i in range(index, len(coins)):
                if coins[i] <= amount < coins[i]*(self.res - count):
                    dfs(i, amount - coins[i], count + 1)
            
        coins.sort(reverse = True)
        self.res = sys.maxsize-1
        dfs(0, amount, 0)
        return self.res if self.res < sys.maxsize-1 else -1






