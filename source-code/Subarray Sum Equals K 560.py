# 560. Subarray Sum Equals K
# ttungl@gmail.com

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # sol 1:
        # use dict to store sums and k.
        # for every element, sums it up
        #   update res by getting value of (sums-k) in dict
        #   increase by 1 of sums.
        # runtime: 83ms
        d = collections.defaultdict(int) 
        d[0] = 1 # init total:k
        res = cur = 0
        for i in nums:
            cur += i
            res += d[cur - k]
            d[cur] += 1 
        return res
    
        # sol 2:
        # runtime:
        
    
    
        
                    
                    
