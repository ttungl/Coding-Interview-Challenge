# 461. Hamming Distance
# ttungl@gmail.com
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # sol 1
        # time O(n) space O(1)
        # runtime 34ms
        return bin(x^y).count('1')
    
        # sol 2
        # runtime: 42ms
        z = x^y
        t = list(bin(z)[2:])
        return t.count('1')

