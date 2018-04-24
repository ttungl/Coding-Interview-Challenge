# 202. Happy Number
# ttungl@gmail.com
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # time O(n) space O(n)
        # runtime: 39 ms
        total, seen = n, set() 
        while total not in seen: # O(1)
            seen.add(total)
            total = sum([int(x)**2 for x in str(total)]) # O(n)
        return total==1
        
        # sol 2: 
        # runtime: 49 ms
        seen = []
        while n not in seen:
            seen.append(n)
            n = sum(int(i)**2 for i in str(n))
        return n==1
        

