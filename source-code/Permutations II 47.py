# 47. Permutations II

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
        # sol 1:
        # time O(n^2) space O(n)
        # runtime: 134ms
        def dfs(nums, permu):
            if len(nums)==0:
                res.append(permu)
            [dfs(nums[:i]+nums[i+1:], permu + [nums[i]]) for i in range(len(nums)) if i==0 or nums[i]!=nums[i-1]]
        res = []
        dfs(sorted(nums), [])
        return res
        

        # sol 2:
        # runtime: 141ms
        res = [[]]
        for n in nums:
            tmp = []
            for l in res:
                for i in xrange(len(l)+1):
                    tmp.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break  # handles duplication
            res = tmp
        return res

        
        # sol 3:
        # runtime: 92ms
        res = [[]]
        for n in sorted(nums): # [1,1,2]
            res = [s[:i]+[n]+s[i:] # [s[:i]+[1]+s[i:]]
                   for s in res 
                    for i in range((s+[n]).index(n)+1)]
        return res
        