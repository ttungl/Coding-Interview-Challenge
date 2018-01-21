# 263. Ugly Number

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # sol 1: positive number and contain primes.
        # runtime: 35 ms
        p = [2, 3, 5]
        for i in p:
            while num%i==0 and num > 0: 
                num /= i
        return num==1
        