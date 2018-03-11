# subsets 78

# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #######
        # sol 1: iterative
        # runtime: 42ms
        res = [[]]
        for i in nums:
            res += [j + [i] for j in res]
        return res
    
    	#######
        # sol 2: DFS recursively
        # runtime: 42ms
        def DFS(nums, index, path, res):
            res.append(path)
            [DFS(nums, i + 1, path + [nums[i]], res) for i in range(index, len(nums))]
        res = []    
        DFS(nums, 0, [], res)
        return res
        
        