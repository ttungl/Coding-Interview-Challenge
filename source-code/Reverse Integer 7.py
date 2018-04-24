# 7. Reverse Integer
# ttungl@gmail.com
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output:  321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # sol 1:
        # runtime: 54ms
        if not x: 
            return 0
        sign = res = 0
        y = str(x)
        if y[0] == "-": 
            sign = 1
            y = y[1:]
        z = y[::-1]
        if sign == 1:
            res = (-1) * int(''.join(z)) 
        else:
            res = int(''.join(z)) 
        # overflow    
        if -2147483648 <= res < 2147483647: 
            return res
        else: 
            return 0
        
        # sol 2:
        # runtime: 56ms
        s = str(x)
        max_bound = sys.maxsize
        res = (int("-"+ s[1:][::-1]) if s[0] == "-" else int(s[::-1]))
        return res if -2147483648 <= res < 2147483647 else 0
        
            
            
        