# Combination Sum 39
# ttungl@gmail.com
# given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # sol 1:
        # Use DFS backtracking
        # in the range of (index, length of candidates),
        # after hitting the base case, return.
        # Runtime: 175ms
        def DFS(candidates, target, index, path, res):
            if target < 0: return 
            if target ==0: # hit base case 
                res.append(path)
                return
            for i in range(index, len(candidates)): # each entire loop for each call
                DFS(candidates, target - candidates[i], i, path + [candidates[i]], res)
            
        res, path = [], []
        DFS(sorted(candidates), target, 0, path, res)
        return res    
        
        # sol 2:
        # DFS optimized
        # runtime: 85ms
        def DFS(nums, target, index, path, res):
            if target == 0: # end
                res.append(path)
                return
            while index >=0 and index < len(nums) and nums[index] <= target:
                DFS(nums, target - nums[index], index, path + [nums[index]], res)
                index += 1
            
        res, path = [], []
        DFS(sorted(candidates), target, 0, path, res)
        return res
        
        
        
        
        
        