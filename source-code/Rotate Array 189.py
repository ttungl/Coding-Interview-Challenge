# 189. Rotate Array

# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

# Space O(1) is a must.


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # sol 1
        # time O(n) space O(1)
        # runtime: 93ms
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
        # sol 2
        # time O(n) space O(1)
        # runtime: 74ms
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        
        # sol 3
        # time O(n) space O(1)
        # runtime: 292ms
        while k>0:
            tem = nums.pop(-1)
            nums.insert(0,tem)
            k-=1