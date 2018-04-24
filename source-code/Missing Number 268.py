# 268. Missing Number
# ttungl@gmail.com
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1

# Input: [3,0,1]
# Output: 2
# Example 2

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1
        # runtime 77ms
        nums.sort()
        for i in range(len(nums)):
            if nums[i] - i != 0: # if value != its index: return index.
                return i
        return len(nums)
        
        # sol 2:
        # binary search
        # time O(log n) space O(1)
        # runtime: 72ms
        nums.sort() # in-place sort.
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo)/2
            if nums[mid] > mid: hi = mid
            else: lo = mid + 1
        return lo
    
        # sol 3: 
        # xor
        # time O(n) space O(1)
        # runtime: 53ms
        n = len(nums)
        for i in range(len(nums)): # i,n=(0,3);(1,3);(2,3). 
            n = n^i 			   # n=3=3^0; 1=0^1; 3=1^2.
            n = n^nums[i] 		   # n=0=3^3; 1=1^0; 2=3^1.	
        return n # 2

