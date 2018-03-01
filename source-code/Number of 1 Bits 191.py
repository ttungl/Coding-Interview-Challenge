# 191. Number of 1 Bits

# Write a function that takes an unsigned integer and returns the number of ’1' bits it has 
# (also known as the Hamming weight).

# For example, the 32-bit integer ’11' has 
# binary representation 00000000000000000000000000001011, 
# so the function should return 3.

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # sol 1:
        # runtime: 44ms
        return bin(n).count("1")
    
        # sol 2:
        # runtime: 40ms
        res = 0
        while n > 0:
            if n%2 == 1:
                res += 1
            n /= 2
        return res
        
    
        