# 60. Permutation Sequence
# ttungl@gmail.com
# The set [1,2,3,…,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.



class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # sol 1:
        # runtime: 52ms
        # compute n!
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        # range of n    
        nums = map(str, range(1, n + 1))
        permus = ''
        k -= 1
        # 
        for i in range(1, n+1)[::-1]:
            factorial /= i
            index = k / factorial 
            permus += nums[index]
            nums = nums[:index] + nums[index+1:]
            k -= index * factorial
        return permus
        
        
        # sol 2:
        # find index of current digit using divmod, k/(n-1)!
        # return index of current digit (quotient~ current index + remainder~ index k for (n-1) nums)
        # runtime: 36ms
        nums = map(str, range(1, n+1))
        permus = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n)) 
            permus += nums[index]
            nums = nums[:index] + nums[index+1:]
        return permus
        
        






