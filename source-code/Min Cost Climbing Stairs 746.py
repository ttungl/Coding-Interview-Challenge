# 746. Min Cost Climbing Stairs

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # sol 1: 
        # time O(n) space O(1)
        # runtime: 35ms
        if not cost or len(cost)==1: 
        	return 0
        min0, min1 = cost[0], cost[1]    
        for i in range(2, len(cost)):
            min0, min1 = min1, min(min0, min1) + cost[i]
        return min(min0, min1)


        # sol 2:
        # time O(n) space O(1)
        # runtime: 43ms
        s = [0]
        for c in cost:
            s = c + min(s), s[0]
        return min(s)

            
        
        
        


