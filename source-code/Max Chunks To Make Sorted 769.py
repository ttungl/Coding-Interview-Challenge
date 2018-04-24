# 769. Max Chunks To Make Sorted
# ttungl@gmail.com
# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], 
# we split the array into some number of "chunks" (partitions), 
# and individually sort each chunk.  After concatenating them, 
# the result equals the sorted array.

# What is the most number of chunks we could have made?

# Example 1:
# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will 
# result in [3, 4, 0, 1, 2], which isn't sorted.

# Example 2:
# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest 
# number of chunks possible.


class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # sol 1
        # time O(n^2) space O(1)
        # runtime: 31ms
        maxcount, res = 0, 0
        for i,v in enumerate(arr):
            maxcount = max(maxcount, v)
            res += maxcount == i
        return res
        
        # sol 2
        # time O(n^2) space O(1)
        # runtime: 32ms
        return sum(max(arr[:i+1])==i for i in range(len(arr)))
    
        # sol 3
        # runtime: 32ms
        maxcount, res = -1, 0
        for i,v in enumerate(arr):
            maxcount = max(maxcount, v)
            if maxcount==i:
                res+=1
        return res