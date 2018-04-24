# 233. Number of Digit One
# ttungl@gmail.com
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers 
# less than or equal to n.

# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # sol 1:
        # runtime: 28ms
        if n <= 0:
            return 0
        q, x, res = n, 1, 0
        while q > 0:
            digit = q % 10 # extract the last digit in q.
            q /= 10 # get the left part.
            res += q * x #
            if digit == 1:  # abc*1000 + xyz + 1
                res += n % x + 1
            elif digit > 1: # abc*1000 + 1000
                res += x
            x *= 10
        return res
    
    
        # sol 2:
        # runtime: 32ms
        if n <= 0:
            return 0 
        if n == 1:
            return 1
        m, res = 1, 0
        while(m <= n):
            a = n / m
            b = n % m
            res += (a + 8) / 10 * m ## ?!
            if a % 10 == 1:
                res += (b + 1)
            m = m * 10
        return res
    
    
        # sol 3:
        # idea from @cdai
		# Basic idea: count number of combination of 1 at each digit in two cases: prefix 
		# appears or not. Eg.3101592:
		# 	1) one at hundreds:      
		# 		1 (< 5): [1~3101]1[0~99]. So res = 3101 * 100 + 100 
		# 			(Safe since 31011XX never be greater than 31015XX)
		# 	2) one at thousands:     
		# 		1 (= 1): [1~310]1[0~592]. 
		# 			So res = 310 * 1000 + (592 + 1) 
		# 			(Unsafe if prefix is 0, it must be <= 1592)
		# 	3) one at ten thousands: 
		# 		1 (> 0): [1~30]1[0~9999]. 
		# 			So res = 30 * 10000 (If prefix is 0, no 1 digit number exist)
        # runtime: 28ms
        if n <= 0: 
        	return 0
        if n == 1: 
        	return 1
        res, i, q = 0, 1, n
        while i <= n:
            prefix = n / (i * 10)
            current = q % 10
            suffix = n % i
            res += prefix * i
            if current > 1:
                res += i
            elif current == 1:
                res += suffix + 1
            q /= 10
            i *= 10
        return res
    
        