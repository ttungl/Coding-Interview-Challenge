# 123. Best Time to Buy and Sell Stock III
# ttungl@gmail.com

# find the maximum profit to complete at most two transactions.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # runtime: 60ms       
        if not prices: return 0
        b1 = b2 = -sys.maxint
        s1 = s2 = 0
        for i in prices:
        	s1 = max(s1, b1 + i)
        	b1 = max(b1, -i)
        	s2 = max(s2, b2 + i)
        	b2 = max(b2, s1 - i)
        return s2
