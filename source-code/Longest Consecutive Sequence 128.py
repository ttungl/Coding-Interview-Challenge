# 128. Longest Consecutive Sequence

# Given an unsorted array of integers, find the length of the longest consecutive
# elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1
        # array
        # time O(n) space O(1)
        # runtime: 36ms
        nums = set(nums) # O(n); return set of unique elements in nums. 
        res = 0
        for i in nums:
            if i-1 not in nums: # i-1=1-1=0; 
                j = i+1			# j=1+1=2; adjacent node.
                while j in nums: # next consecutive adjacents.
                    j+=1
                # stop at the first j not in the set.
                res = max(res, j-i) # update max length.
        return res
    	
        # sol 2
        # union find
        # time O(n) space O(n)
        # runtime 48ms
        d, res = {}, 0
        for i in range(len(nums)):
            if nums[i] not in d: # check if node in dict.
                d1, d2 = d.get(nums[i]-1, 0), d.get(nums[i]+1, 0) # get values of nodes in +/-1 from dict, return 0 if not found
                d[nums[i]] = d[nums[i]-d1] = d[nums[i]+d2] = d1 + d2 + 1 # update it and its neighbors ~ length.
                res = max(res, d[nums[i]]) # update max length.
        return res
    
        
                
            
        
        
                
            
                
                
                
        
        
                
            
                
                
                

