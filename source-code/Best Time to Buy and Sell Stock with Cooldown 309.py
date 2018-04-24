# 309. Best Time to Buy and Sell Stock with Cooldown
# ttungl@gmail.com

# [buy-sell-cooldown] with max profit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy-sell-cooldown;
        # runtime: 45ms
        if not prices: return 0
        
        b1 = b0 = -prices[0]
        res = s1 = s2 = 0
        
        for i in prices:
            res = max(s1, b1 + i)
            b0 = max(b1, s2 - i) 
            b1 = b0
            s2 = s1
            s1 = res
        return res

