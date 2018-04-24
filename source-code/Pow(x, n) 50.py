# 50. Pow(x, n)
# ttungl@gmail.com
# E.g. 	Pow(2.000,10) = 1024
# 	 	Pow(2.100, 3) = 9.261

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # sol 1:
        # recursive
        # runtime: 43ms
        if not n:
            return 1
        if n < 0: # flip it.
            n = -n
            x = 1/x
        if n%2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x * self.myPow(x*x, n/2)
        
        # sol 2
        # bit manipulation
        # runtime: 45ms
        if not n: 
            return 1
        if n < 0:
            n = -n
            x = 1/x
        res = 1
        while n:
            if n & 1: ## same as (n%2)
                res *= x
            x *= x
            n>>=1 ## same as (n/=2)
        return res
    
        
        
        
    
        
        
        





