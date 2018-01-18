# 122. Best Time to Buy and Sell Stock II

# max profit of multiple transactions

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # runtime: 35ms
        if not prices: return 0
        res = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]: 
                res += prices[i] - prices[i-1]
        return res
        


