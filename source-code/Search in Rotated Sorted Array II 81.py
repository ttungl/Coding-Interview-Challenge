# Search in Rotated Sorted Array II 81

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # use binary search
        # tricky part is to increase the left until left=mid and nums[mid]!=nums[left]
        # runtime: 32ms
        left, right = 0, len(nums)-1
        
        while left <= right:
            
            mid = left + (right-left)/2
            
            if nums[mid] == target:
                return True
            
            # tricky line!!
            while left < mid and nums[mid] == nums[left]: left+=1
             
            if nums[mid] >= nums[left]:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
        
        