# 324. Wiggle Sort II
# ttungl@gmail.com
# Given an unsorted array nums, reorder it such that 
# nums[0] < nums[1] > nums[2] < nums[3]....

# Example:
# (1) Given nums = [1, 5, 1, 1, 6, 4], 
# one possible answer is [1, 4, 1, 5, 1, 6]. 

# (2) Given nums = [1, 3, 2, 2, 3, 1], 
# one possible answer is [2, 3, 1, 3, 1, 2].

# Note:
# You may assume all input has valid answer.

# Follow Up:
# Can you do it in O(n) time and/or in-place with 
# O(1) extra space?

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # sol 1:
        # wiggle constraint: n0 < n1 > n2 < n3 > n4 ...
        # note: 
        #   nums[::2] means even indices (0,2,4..)
        #   nums[1::2] means odd indices (1,3,5..)
        # runtime: 210ms
        nums.sort() # takes O(n log n)
        n = len(nums)
        m = (n+1)//2
        nums[::2], nums[1::2] = nums[:m][::-1], nums[m:][::-1]
        
        
        # sol 2:
        # runtime
        
        def find_median(nums, lo, hi): # time O(n)
            i = j = k = lo+1
            mid = n//2
            pivotal = nums[lo]
            while k <= hi:
                if nums[k] < pivotal:
                    nums[k], nums[j] = nums[j], nums[k]
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                    k += 1
                elif nums[k] > pivotal: 
                    k += 1
                else:
                    nums[j], nums[k] = nums[k], nums[j]
                    j += 1
                    k += 1
            
            nums[lo], nums[i-1] = nums[i-1], nums[lo]
            if i-1 <= mid < j:
                return nums[mid]
            if mid >= j:
                return find_median(nums, j, hi)
            else:
                return find_median(nums, lo, i-2)
            
        n = len(nums)
        m = (n+1)//2        
        find_median(nums, 0, len(nums)-1) # take O(n) in-place
        nums[::2], nums[1::2] = nums[:m][::-1], nums[m:][::-1]
        
        
        
        




