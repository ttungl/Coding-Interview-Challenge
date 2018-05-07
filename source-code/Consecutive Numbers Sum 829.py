# 829. Consecutive Numbers Sum

# Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

# Example 1:

# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# Example 2:

# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# Example 3:

# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# Note: 1 <= N <= 10 ^ 9.


class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # sol 1:
        # key:
        # sequence: x + (x+1) + (x+2)+...+ k-term = N
        # -> kx + k(k-1)/2 = N
        # -> kx = N - k(k-1)/2 > 0
        # derive to: k < sqrt(2N)
        # time O(sqrt(n)) space O(1)
        # runtime: 188ms
        count = 1
        for k in range(2, int((2*N)**0.5)+1):
            if (N - (k*(k-1)/2)) % k == 0: 
            	count += 1
        return count
     

        
