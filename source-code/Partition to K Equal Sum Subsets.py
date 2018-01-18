# 698. Partition to K Equal Sum Subsets

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/


# time complexity O(n * k)
# space complexity O(n)
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sumnums = 0
        for num in nums:  # sum all of elements in nums
            sumnums += num

        if k <= 0 or sumnums%k != 0: # check base cases
            return False

        visited = [0]*len(nums) # mark the visited elements in nums
        
        return self.canPartition(nums, visited, 0, k, 0, 0, sumnums/k)
    
    def canPartition(self, nums, visited, index, k, curSum, curElem, target):
        if k==1: return True
        
        if curSum == target and curElem >0: # go to next recursion when it meets target and guarantees elements exist in subset.
            return self.canPartition(nums, visited, 0, k-1, 0, 0, target)
        
        for i in range(index, len(nums)): # DFS
            if visited[i]==0:
                visited[i] = 1
                if self.canPartition(nums, visited, i+1, k, curSum+nums[i], curElem+1, target): 
                    return True
                visited[i] = 0
        return False
                
    

        
                
        