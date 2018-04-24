# 55. Jump Game
# ttungl@gmail.com

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false.



class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sol 1:
        # update max index that can be reachable.
        # runtime: 51ms
        maxcur = 0
        for i in range(len(nums)):
        	maxcur = max(maxcur, i + nums[i])
            if i > maxcur:
                return False
        return True
    
        # sol 2:
        # runtime: 77ms
        target = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= target:
                target = i
        return target == 0
        
        
                
            