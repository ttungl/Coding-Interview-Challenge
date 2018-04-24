# 762. Prime Number of Set Bits in Binary Representation
# ttungl@gmail.com
# Input: L = 6, R = 10
# Output: 4
# Explanation:
# 6 -> 110 (2 set bits, 2 is prime)
# 7 -> 111 (3 set bits, 3 is prime)
# 9 -> 1001 (2 set bits , 2 is prime)
# 10->1010 (2 set bits , 2 is prime)

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def is_prime(n): 
        	return all(n%j for j in range(2, int(n**0.5)+1)) and n>1
        count = 0
        for i in range(L, R+1):
            if is_prime(bin(i).count("1")): count+=1
        return count

