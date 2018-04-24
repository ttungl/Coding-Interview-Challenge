# 788. Rotated Digits

# ttungl@gmail.com
# X is a good number if after rotating each digit individually by 180 degrees, 
# we get a valid number that is different from X. A number is valid if each digit r
# emains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to 
# each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate 
# to any other number.

# Now given a positive number N, how many numbers X from 1 to N are good?

# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:

# N  will be in range [1, 10000].


# import itertools
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # sol 1
        # runtime: 398ms
        s1 = set([1, 8, 0])
        s2 = set([1, 8, 0, 6, 9, 2, 5])
        def isGood(x):
            s = set([int(i) for i in str(x)])
            return s.issubset(s2) and not s.issubset(s1)
        return sum(isGood(i) for i in range(N + 1))
        
        
        # sol 2:
        # runtime: 280ms
        res, s1, s2 = 0, [3, 4, 7], [2, 5, 6, 9]
        for i in range(1, N + 1):
            if any(True if str(k) in str(i) else False for k in s1): continue
            if any(True if str(h) in str(i) else False for h in s2): res+=1   
        return res
    
        # sol 3:
        # runtime: 69ms
        res = 0
        for i in range(1, N+1):
            s = str(i)
            if '3' in s or '7' in s or '4' in s: 
                continue
            if '2' in s or '5' in s or '6' in s or '9' in s:
                res += 1
        return res
        
        