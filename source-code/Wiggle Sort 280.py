# 280. Wiggle Sort
# ttungl@gmail.com
# Given an unsorted array nums, reorder it in-place 
# such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# For example, given nums = [3, 5, 2, 1, 6, 4], 
# one possible answer is [1, 6, 2, 5, 3, 4].


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # sol 1:
        # wiggle constraint: nums[i-1] <= nums[i] >= nums[i+1]
        # otherwise, swap them.
        # runtime: 120ms
        if not nums: 
            return
        n = len(nums)
        for i in range(1, n, 2):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            if i+1 < n and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
        # sol 2:
        # runtime: 126ms
        if not nums: 
            return
        for i in range(len(nums)-1):
            if (i%2 == 0 and (nums[i] > nums[i+1])) or (i%2 == 1 and nums[i] < nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        

        # sol 3:
        # runtime: 115ms
        m = (len(nums)+1)//2
        nums.sort()
        nums[::2], nums[1::2] = nums[:m][::-1], nums[m:][::-1] 
            