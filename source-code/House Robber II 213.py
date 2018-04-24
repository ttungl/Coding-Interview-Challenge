# House Robber II 213
# ttungl@gmail.com
# After robbing those houses on that street, the thief has found himself 
# a new place for his thievery so that he will not get too much attention. 
# This time, all houses at this place are arranged in a circle. 
# That means the first house is the neighbor of the last one. 
# Meanwhile, the security system for these houses remain the same 
# as for those in the previous street.

# Given a list of non-negative integers representing the amount 
# of money of each house, determine the maximum amount of money 
# you can rob tonight without alerting the police.


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1
        # runtime: 32ms
        def robsub(nums):
            now, prev = 0, 0
            for i in nums:
                now, prev = max(now, prev + i), now
            return now
        # corner case: nums[len(nums)!= 1:] means that len(nums)!=1 will be false =0 and true=1
        return max(robsub(nums[len(nums)!= 1:]), robsub(nums[:-1]))
        
        # sol 2:
        # runtime: 32ms
        def robsub(nums):
            now, prev = 0, 0
            for i in nums:
                now, prev = max(now, prev + i), now
            return now
        return max(robsub(nums[:-1]), robsub(nums[1:])) if len(nums) is not 1 else nums[0]
        
        

        