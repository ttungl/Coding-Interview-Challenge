# 714. Best Time to Buy and Sell Stock with Transaction Fee


# idea: buy-sell-fee;

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # t0: sell; t1: buy;
        # runtime: 258ms
        t0, t1 = 0, -sys.maxsize
        
        for p in prices:
            t0_temp = t0 
            t0 = max(t0, t1 + p) # sell
            t1 = max(t1, t0_temp - p - fee) # buy
        return t0