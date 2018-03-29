# 70. Climbing Stairs

# Takes n steps to reach to the top.
# each time can either climb 1 or 2 steps. 
# #distinct ways can you climb to the top?
# n: a positive integer.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # sol 1:
        # runtime: 36ms
        s1, s2, res = 0, 1, 0
        for i in range(n):
            res = s1 + s2
            s1, s2 = s2, res
        return res
            

