# 371. Sum of Two Integers

# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # sol 1:
        # runtime: 40ms
        return sum([a, b])
    
        # sol 2:
        # runtime:
        def add(a, b):
            if not a or not b:
                return a or b
            return add((a ^ b), (a & b) << 1)
        if a * b < 0: # either one less than zero
            if a > 0:
                a, b = b, a
            if -a == b: return 0
            if -a < b: return -add(-a, -b)
        return add(a, b)
            