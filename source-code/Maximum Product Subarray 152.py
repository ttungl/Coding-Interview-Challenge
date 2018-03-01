# 152. Maximum Product Subarray


# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1:
        # time O(n) space O(1)
        # runtime: 44ms
        if not nums: return 0
        res = minlst = maxlst = nums[0]
        for i in nums[1:]:
            if i < 0:
                maxlst, minlst = minlst, maxlst
            maxlst = max(i, maxlst * i)
            minlst = min(i, minlst * i)
            res = max(res, maxlst)
        return res
        
        