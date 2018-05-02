# 309. Best Time to Buy and Sell Stock with Cooldown
# ttungl@gmail.com

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
# (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:

# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]

# [buy-sell-cooldown] with max profit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy-sell-cooldown;
        # runtime: 45ms
        if not prices:
            return 0
        
        b1 = b2 = -prices[0]
        res = s1 = s2 = 0

        for i in prices:
            res = max(res, b1+i)
            b2 = max(b1, s2-i)
            
            b1, s2, s1 = b2, s1, res

        return res

