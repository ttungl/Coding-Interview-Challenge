# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None and len(nums)==0: return None
        
        left=0
        right=len(nums)-1
        
        while left < right-1: # useful (left < right-1): stops at left=right-1: left and right next to each other
            mid = left + (right - left)/2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
            
        if nums[left] > nums[right]:
            return nums[right]
        return nums[left]
    
    
        