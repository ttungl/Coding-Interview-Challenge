# 45. Jump Game II


# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# Note:
# You can assume that you can always reach the last index.


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1:
        # Use two pointers "start" and "end" to store current 
        # range of the current index. 
        # For each move, find the farest index that can be 
        # reached in one move of the current range [start, end+1].
        # runtime: 60ms
        start = end = minJump = 0
        while end < len(nums) - 1:
            minJump += 1
            start, end = end + 1, max([i + nums[i] for i in range(start, end + 1)])
        return minJump



        # sol 2:
        # keep track of the index i and maxcur_index.
        # runtime: 73ms
        maxcur = cur = minJump = 0
        for i in range(len(nums)-1):
            maxcur = max(maxcur, i + nums[i])
            if i == cur:
                minJump += 1
                cur = maxcur
        return minJump
    
        
        
    
    
            
        
        
        
        
        






