# 823. Binary Trees With Factors


# Given an array of unique integers, each integer is strictly greater than 1.

# We make a binary tree using these integers and each number may be used for any number of times.

# Each non-leaf node's value should be equal to the product of the values of it's children.

# How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

# Example 1:

# Input: A = [2, 4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# Example 2:

# Input: A = [2, 4, 5, 10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].


class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # sol 1:
        # DP
        # dp[i] = sum(dp[j] * dp[i/j])
        # res = sum(dp[i])
        # time O(n*m) space O(n)
        # runtime: 636ms
        A.sort()
        dp = collections.defaultdict(int)
        for i,v in enumerate(A):
            dp[v] = 1
            for u in A[:i]:
                if v % u == 0 and v/u in dp: # find all factors.
                    dp[v] += dp[u] * dp[v/u]
        return sum(dp.values())%(10**9 + 7)
        
        
        
        



