# 154. Find Minimum in Rotated Sorted Array II

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# The array may contain duplicates.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1:
        # binary search
        # runtime: 55ms
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left)/2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else: # same values on left and right
                right -= 1
        return nums[left]
    
        # sol 2:
        # runtime: 50ms
        if not nums:
            return 0
        res = None
        for num in nums:
            if res == None: 
                res = num
            if num < res:
                return num
        return res
                