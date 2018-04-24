# 300. Longest Increasing Subsequence
# ttungl@gmail.com
# Given an unsorted array of integers, 
# find the length of longest increasing subsequence.

# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], 
# so, return 4.

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use DP 
        # if (n=) nums[i] > dp[i], then append it to dp and increase count.
        # if dp[i-1] < nums[i] < dp[i]: update dp[i].
        # runtime: 32ms

        if not nums: return 0

        dp = [0]*len(nums)

        count = 0
        
        for n in nums:
        	i, j = 0, count
        	
        	while i!=j: # binsearch
        		mid = (i+j)//2
        		if dp[mid] < n: 
        			i = mid + 1
        		else: j = mid 

        	dp[i] = n
        	if i==count: count+=1
        return count
        

