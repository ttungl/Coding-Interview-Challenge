# 238. Product of Array Except Self
# ttungl@gmail.com
# Given an array of n integers where n > 1, nums, return an array output such that output[i] 
# is equal to the product of all the elements of nums except nums[i].

# Solve it without division and in O(n).

# For example, given [1,2,3,4], return [24,12,8,6].

# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count 
# as extra space for the purpose of space complexity analysis.)


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sol 1:
        # time O(n) space O(1)
        # runtime: 168ms
        res, p, n = [], 1, len(nums)
        for i in nums:
            res.append(p)
            p*=i
        p=1
        for i,v in enumerate(nums[::-1]):
            res[n-i-1] *=p
            p *=v
        return res
        
        # sol 2:
        # time O(n) space O(1)
        # runtime: 183ms
        p1, p2, n = 1, 1, len(nums)
        res = [1]*n
        for i in range(n):
            res[i] *= p1; res[n-i-1] *= p2

            p1 *= nums[i]; p2 *= nums[n-i-1]

        return res
            
            
        
        
        
        


