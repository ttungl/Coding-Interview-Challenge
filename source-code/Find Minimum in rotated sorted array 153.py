# 153. Find Minimum in Rotated Sorted Array


# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1
        # binary search
        # runtime: 34ms
        left, right = 0, len(nums)-1
        while left < right-1:
            mid = left + (right - left)/2
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
        if nums[left] > nums[right]:
            return nums[right]
        return nums[left]
    
        # sol 2:
        # DFS
        # runtime: 34ms
        def dfs(nums, left, right):
            mid = left + (right - left)/2
            if nums[mid] > nums[right]:
                return dfs(nums, mid+1, right)
            elif nums[mid] < nums[right]:
                return dfs(nums, left, mid)
            else:
                return nums[mid]
        left, right = 0, len(nums)-1
        return dfs(nums, left, right)
        
        