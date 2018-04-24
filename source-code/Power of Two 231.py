# 231. Power of Two
# ttungl@gmail.com
# Given an integer, write a function to determine if it is a power of two.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # sol 1:
        # runtime: 46ms
        return (n & (n-1)==0) and n > 0
    
        # sol 2
        # runtime: 42ms
        if n <= 0: 
            return False
        while n%2 == 0:
            n>>=1
        return n==1
        

