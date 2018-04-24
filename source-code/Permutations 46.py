# 46. Permutations
# ttungl@gmail.com
# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]



class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sol 1
        # runtime: 65ms
        return nums and [p[:i] + [nums[0]] + p[i:] 
                         for p in self.permute(nums[1:]) 
                         	for i in range(len(nums))] or [[]]
        
        # sol 2:
        # runtime: 70ms
        def dfs(nums, path):
            if not nums:
                res.append(path)
                # return # backtracking
            for i in range(len(nums)):
                if i==0 or nums[i]!=nums[i-1]:
                    dfs(nums[:i] + nums[i+1:], path + [nums[i]])
        res = []
        dfs(sorted(nums), [])
        return res
            
        