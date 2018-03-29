# 121. Best Time to Buy and Sell Stock

# max profit of one transaction

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # optimized solution
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
    
        
        
        
                
            
        
        


