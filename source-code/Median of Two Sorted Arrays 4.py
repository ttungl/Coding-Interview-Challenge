# 4. Median of Two Sorted Arrays
# ttungl@gmail.com
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # sol 1:
        # runtime: 97ms
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n < 1:
            return 0.0
        if n % 2 == 1:
            return float(nums[n//2])
        else:
            return sum(nums[n//2-1:n//2+1])/2.0
        
        # sol 2:
        # use priority queue
        # time O(nlogn) space O(n)
        # runtime: 385ms
        nums = nums1 + nums2
        loHeap, hiHeap = [], []
        for num in sorted(nums):
            heappush(loHeap, -heappushpop(hiHeap, num))
            if len(loHeap) > len(hiHeap):
                heappush(hiHeap, -heappop(loHeap))
        if len(loHeap) >= len(hiHeap):
            return (hiHeap[0] - loHeap[0])/2.0
        return float(hiHeap[0])
        
            
            
            
                
        
        
        
        
        