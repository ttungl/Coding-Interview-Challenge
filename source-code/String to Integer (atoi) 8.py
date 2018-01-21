# String to Integer (atoi) 8

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # solution: use sign and add digits.
        # runtime: 69 ms
        
        # base case
        if len(str)==0: 
            return 0
        
        # str.strip(): removes heading and trailing of the string. Note: tuple(str) doesn't work.
        str = list(str.strip()) 
        
        # check sign
        sign = 1
        if str[0] == '-':
            sign = -1
            del str[0]
            
        elif str[0]=='+':
            sign = 1
            del str[0]
        
        # add up digits
        res, i = 0, 0
        while i< len(str) and str[i].isdigit():
            res = res*10 + (ord(str[i]) - ord('0'))
            i+=1
        
        return max(-2**31, min(sign*res, 2**31-1))