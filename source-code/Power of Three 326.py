# 326. Power of Three



# Given an integer, write a function to determine if it is a power of three.

# Follow up:
# Could you do it without using any loop / recursion?

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # sol 1: follow-up 
        # runtime: 193ms
        # Use 3^19 (is 1162261467), bcos 3^20 is bigger than int.  
        return n > 0 and (3**19 % n) == 0
        
        # sol 2:
        # runtime: 205ms
        if n <= 0:
            return False
        while n % 3==0:
            n/=3
        return n==1
        











