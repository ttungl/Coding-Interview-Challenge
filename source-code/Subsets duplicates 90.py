# subsets duplicates 90
# ttungl@gmail.com
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
        ## DFS recursion
        ## runtime: 72ms
        def DFS(nums, index, path, res):
            res.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i]==nums[i-1]: 
                    continue
                DFS(nums, i+1, path + [nums[i]], res)
            
        res = []
        DFS(sorted(nums), 0, [], res)
        return res
        
        ####################
        ## iterative:
        ## runtime: 99ms
        res = [[]]
        for i in sorted(nums):
            res += [j + [i] for j in res if j + [i] not in res]
        return res
        
       