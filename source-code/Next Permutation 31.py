# 31. Next Permutation
# ttungl@gmail.com

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # sol 1:
        # runtime: 54ms
        i = k = len(nums) - 1
        # traverse backward to find first index that meets nums[i-1] < nums[i].
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        j = i
        # reverse from i to n-1.
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1; k -= 1
        # swap if possible 
        # to find next permutation, swapping some positions 
        # that minimizes the increased amount, 
        # which means finding an index k that meets this condition: nums[k] > nums[i]
        if i > 0:
            i -= 1; s = i
            while nums[s] <= nums[i]:
                s += 1
            nums[i], nums[s] = nums[s], nums[i]
            
        # sol 2:
        # runtime:
        
        
            