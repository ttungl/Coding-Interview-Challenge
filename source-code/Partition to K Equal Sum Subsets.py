# 698. Partition to K Equal Sum Subsets

# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Note:

# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.

# time complexity O(n * k)
# space complexity O(n)
class Solution(object):
    # sol 1:
    # DFS
    # runtime: 661ms
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def canPartition(nums, visited, index, k, curSum, curElem, target):
            if k==1: 
                return True

            # go next recursion if meet target, guarantees elems exist in subset.
            if curSum == target and curElem >0: 
                return canPartition(nums, visited, 0, k-1, 0, 0, target)
            
            for i in range(index, len(nums)): # DFS
                if visited[i]==0:
                    visited[i] = 1
                    if canPartition(nums, visited, i+1, k, curSum+nums[i], curElem+1, target): 
                        return True
                    visited[i] = 0
            return False
        #
        sumnums = sum(nums)
        if k <= 0 or sumnums%k != 0: # check base cases (sumnums must be divisble by k)
            return False
        visited = [0]*len(nums) # mark the visited elements in nums
        return canPartition(nums, visited, 0, k, 0, 0, sumnums/k)
    
    
                
    
    # sol 2:
    # DFS
    # runtime:
    def canPartitionKSubsets(self, nums, k):
        """ """
        if k == 1: 
            return True
        n, sums = len(nums), sum(nums)
        if k > n or sums % k: 
            return False
        target = sums / k
        visited = [0] * n
        sorted(nums)[::-1] 
        #
        def dfs(k, index, sum, cnt):
            if k == 1: 
                return True
            if sum == target and cnt > 0: # backtracking
                return dfs(k-1, 0, 0, 0)

            for i in range(index, n):
                if not visited[i] and sum + nums[i] <= target:
                    visited[i] = 1
                    if dfs(k, i+1, sum + nums[i], cnt + 1): 
                        return True
                    visited[i] = 0
            return False
        
        return dfs(k, 0, 0, 0) # (k-part, index, sum, count) # count checks whether empty list

        
                
        