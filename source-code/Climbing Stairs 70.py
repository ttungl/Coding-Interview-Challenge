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
        # runtime: 26ms
        if n <=2: return n
        one, two, res = 1, 0, 0
        for i in range(n): # n=5
            res = one + two # res=1,2,3,5
            two = one       # two=1,1,2,3
            one = res       # one=1.2,3,5
        return res          # 5

