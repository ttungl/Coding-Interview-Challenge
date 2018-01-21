# 268. Missing Number

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1

# Input: [3,0,1]
# Output: 2
# Example 2

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1: 
        # runtime: 70ms
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] - i != 0:
                return i
        return len(nums)
    
        # sol 2: XOR
        # runtime: 55ms 
        n = len(nums)
        for i in range(n):
            n = n^i
            n = n^nums[i]
        return n

