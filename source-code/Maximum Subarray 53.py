# 53. Maximum Subarray
# ttungl@gmail.com

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1: DP
        # runtime: 50ms
        cur = res = nums[0]
        for n in nums[1:]:
            cur = max(n, n + cur) # max of element and its sum of current max.
            res = max(res, cur) # update final max.
        return res
    
        # sol 2: DP
        # runtime: 46ms
        cur = res = nums[0]
        for n in nums[1:]:
            cur = n if cur < 0 else (n+cur)
            res = max(res, cur)
        return res



