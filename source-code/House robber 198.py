# House robber 198

# Each house has a certain amount of money stashed, the only constraint 
# stopping you from robbing each of them is that adjacent houses have 
# security system connected and it will automatically contact the police 
# if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount 
# of money of each house, determine the maximum amount of money 
# you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use recursive
        # runtime: 31ms
        def robsub(node):
            now, prev = 0,0
            for i in nums:
                now, prev = max(now, prev+i), now
            return now
        # recursive on left and right elements.
        return max(robsub(nums[:-1]), robsub(nums[1:])) 


        # practice:
        # avoid two adjacent house.
        # max money rob.
        # f[0] = nums[0]
        # f[1] = max(nums[0], nums[1])
        # f[k] = max(f[k-2], f[k-1] + nums[k])
        # time O(n) space O(1)
        # runtime: 35ms
        prev, cur = 0, 0
        for i in nums: # flip to avoid adjacent houses.
            prev, cur = cur, max(cur, prev + i)
        return cur