# 47. Permutations II
# ttungl@gmail.com
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # sol 1 
        # runtime: 143ms
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


        # sol 2:
        # time O(n^2) space O(n)
        # runtime: 134ms
        def dfs(nums, path):
            if len(nums)==0: # if not nums
                res.append(path)
            [dfs(nums[:i]+nums[i+1:], path + [nums[i]]) 
            	for i in range(len(nums)) 
            		if i==0 or nums[i]!=nums[i-1]]
        res = []
        dfs(sorted(nums), [])
        return res


        # sol 3:
        # runtime: 141ms
        res = [[]]
        for n in nums:
            tmp = []
            for l in res:
                for i in range(len(l)+1):
                    tmp.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i]==n: 
                    	break  # handles duplication
            res = tmp
        return res

        
        # sol 4:
        # runtime: 92ms
        res = [[]]
        for n in sorted(nums): # [1,1,2]
            res = [s[:i] + [n] + s[i:] # [s[:i]+[1]+s[i:]]
                    for s in res 
                    	for i in range((s + [n]).index(n) + 1)]
        return res
        