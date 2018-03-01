# 338. Counting Bits


# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in 
# their binary representation and return them as an array.

# Example:
# For num = 5 you should return [0,1,1,2,1,2].

# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # sol 1:
        # runtime: 253ms
        res = []
        for i in range(num + 1):
            res.append(bin(i).count("1"))
        return res
            
            
        # sol 2:
        # runtime: >800ms
        def toBinary(i):
            return toBinary(i/2) + [i%2] if i > 1 else [i]
        def countOne(binconv):
            return sum([1 for i in binconv if i == 1])
        res, cnt = [], 0
        for i in range(num+1):
            binConv = toBinary(i)
            cnt = countOne(binConv)
            res.append(cnt)
        return res
        
        
        # sol 3:
        # use DP
        # runtime: 187ms
        if not num: 
            return [0]
        dp = [0] * (num+1)
        dp[0], dp[1] = 0, 1
        for i in range(2, num+1):
            dp[i] = i%2 + dp[i>>1]
        return dp
        








        