# 121. Best Time to Buy and Sell Stock
# ttungl@gmail.com

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# max profit of one transaction

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # optimized solution
        # key: update max res and diff of current and previous update(cur)
        # time O(n); space: O(1)
        # runtime: 32 ms
        if not prices: 
            return 0
        res, cur = 0, prices[0]
        for i in prices[1:]:
            if i > cur: 
                res = max(res, i - cur) 
            else: 
                cur = i # update current
        return res

        # Kadane's algorithm
        # runtime: 52 ms
        cur, res, i = 0, 0, 1
        while i < len(prices):
            cur += prices[i] - prices[i-1]
            cur = max(0, cur)
            res = max(res, cur)
            i+=1
        return res
        
        # TLE*
        i, res = 0, 0
        while i < len(prices):
            for j in range(i, len(prices)):
                if prices[j] > prices[i]: 
                    res = max(res, prices[j] - prices[i])
            i+=1
        return res 
    
        
        
        
                
            
        
        


