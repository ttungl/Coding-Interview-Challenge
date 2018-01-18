# 123. Best Time to Buy and Sell Stock III

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """








# ----

# public int maxProfit(int[] prices) {
#     int bought1 = Integer.MIN_VALUE, bought2 = Integer.MIN_VALUE;
#     int sold1 = 0, sold2=0;
    
#     for(int i : prices){
#         sold1 = Math.max(sold1, bought1 + i);
#         bought1 = Math.max(bought1, -i);
#         sold2 = Math.max(sold2, bought2 + i); 
#         bought2 = Math.max(bought2, sold1 - i);
        
        
#     }
#     return sold2;
# }

