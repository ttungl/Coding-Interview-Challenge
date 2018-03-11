# 90. Subsets II

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sol 1:
        # runtime: 69ms 
        def dfs(nums, idx, p, res): 
            res.append(p)
            for i in range(idx, len(nums)):
                path = p + [nums[i]]
                if path not in res:
                    dfs(nums, i+1, path, res)
        res = []
        dfs(sorted(nums), 0, [], res)
        return res






        
