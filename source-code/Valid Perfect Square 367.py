# 367. Valid Perfect Square

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Returns: True
# Example 2:

# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # sol 1
        # time O(n) space O(1)
        # runtime: 41ms
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
    
        # sol2 :
        # newton's method
        # f(x) = x*x, find x.
        # f'(x) = 2x
        # update x += (num-f(x))/f'(x) += (num-x**2)/2x 
        # x += (num/x - x)/2
        # time
        # runtime
        if num<0: return False
        if num<=1: return True
        n = num//2
        while n*n != num:
            tem = (num/n - n)/2
            if -1 <= tem <= 1: break
            n += tem
        if n*n < num: n+=1
        if n*n > num: n-=1
        return n*n == num
            
        
        
        
        
        
        
        
        
