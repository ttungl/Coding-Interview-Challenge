# 258. Add Digits
# ttungl@gmail.com

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# For example:

# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # sol 1:
        # 10^num = 1 mod 9. 
        # runtime: 48ms
        res = num%9
        return res if res!=0 or not num else 9
                
        # sol 2:
        # runtime: 46ms
        return 0 if not num else num % 9 or 9
        
