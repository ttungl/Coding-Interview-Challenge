# 416. Partition Equal Subset Sum
# ttungl@gmail.com
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sol 1:
        # DFS and memo 
        # target is half of the original sums.
        # use memo_dict to store the results
        # runtime: 51ms
        def search(target, index):
            if target >= sums: 
            	return target == sums
            if target not in memo:
                memo[target] = any(search(target + nums[i], i) for i in range(index + 1, len(nums)))
            return memo[target]
        #
        if not nums: return True 
        sums = sum(nums)
        if sums % 2 or max(nums) > sums/2: 
        	return False

        sums >>= 1 # means: sum/=2
        memo = collections.defaultdict(int)
        sorted(nums)[::-1]
        
        return any(search(v, i) for i,v in enumerate(nums))
        

            
        



        

