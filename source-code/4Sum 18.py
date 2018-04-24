# 18. 4Sum
# ttungl@gmail.com

# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # sol 1:
        # runtime: 105ms
        def dfs(nums, target, k, cur, res):
            if len(nums) < k or k < 2 \
                or target < nums[0]*k or target > nums[-1]*k:
                	return []
            if k == 2: # two pointers in a sorted nums.
                l, r = 0, len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(cur + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l-1]==nums[l]: l += 1
                    elif s < target: l += 1
                    else: r -= 1
            else:
                for i in range(len(nums)-k+1):
                    if i==0 or (i > 0 and nums[i-1] != nums[i]):
                        dfs(nums[i+1:], target-nums[i], k-1, cur+[nums[i]], res)
            return res
        
        res = []
        if not nums: return []
        return dfs(sorted(nums), target, 4, [], res)
        