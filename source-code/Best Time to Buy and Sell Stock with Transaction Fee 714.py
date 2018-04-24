# 714. Best Time to Buy and Sell Stock with Transaction Fee
# ttungl@gmail.com

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
        
        for i in prices:
            t0_temp = t0 
            t0 = max(t0, t1 + i) # sell
            t1 = max(t1, t0_temp - i - fee) # buy
        return t0