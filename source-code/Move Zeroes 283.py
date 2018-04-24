# 283. Move Zeroes
# ttungl@gmail.com

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # sol 1:
        # runtime: 86ms
        i = 0
        for num in nums:
            if num!=0:
                nums[i] = num
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1
        
        # sol 2
        # runtime: 58ms
        j = 0
        for i, num in enumerate(nums):
            if num!=0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        
        





