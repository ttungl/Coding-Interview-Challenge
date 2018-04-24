# Search in Rotated Sorted Array 33
# ttungl@gmail.com
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # use binary search
        # runtime: 36ms
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left)/2
            
            if nums[mid] == target: 
                return mid
            
            if nums[mid] >= nums[left]: # sorted array
                if nums[mid] >= target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            else: # rotated sorted array
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
