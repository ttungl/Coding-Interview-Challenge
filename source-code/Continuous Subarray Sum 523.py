# 523. Continuous Subarray Sum
# ttungl@gmail.com

# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
# Note:
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit integer.




class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # sol 1:
        # time O(n^2) space O(n)
        # runtime: 892ms
        if not nums: 
            return False
        if k < 0: k = -k
        dp = [0]*(len(nums)+1)
        
        for i in range(1, len(nums)+1): # prefix 
            dp[i] = dp[i-1] + nums[i-1]
            
        for i in range(len(nums)):
            for j in range(i+2, len(nums) + 1):
                if (k == 0 and dp[j]-dp[i]==0) \
                    or (k > 0 and (dp[j]-dp[i]) % k==0):
                        return True
        return False
            
            
        # sol 2:
        # time O(n) space O(n)
        # runtime: 52ms
        seen = collections.defaultdict(int)
        seen[0] = -1 # init sums:k
        res = 0
        for i, v in enumerate(nums):
            res = (res + v) % k if k else (res + v)
            if res not in seen: 
            	seen[res] = i
            if i - seen[res] > 1: 
            	return True
        return False
            
        
        
        
        
        
        
        