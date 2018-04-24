# 41. First Missing Positive
# ttungl@gmail.com
# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1
        # runtime: 36ms
        n = len(nums)
        for i in range(n):
            if nums[i] < 1:  
                nums[i] = n+1

        for i in range(n):
            x = abs(nums[i])
            if 0 < x <= n and nums[x-1] > 0:
                nums[x-1] = -nums[x-1] # swap

        for i in range(n):
            if nums[i] > 0:
                return i+1

        return n+1
        
        
        


        
        
