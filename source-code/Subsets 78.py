# subsets 78


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
            [DFS(nums, i+1, path+[nums[i]], res) for i in range(index, len(nums))]
        res = []    
        DFS(nums, 0, [], res)
        return res
        
        