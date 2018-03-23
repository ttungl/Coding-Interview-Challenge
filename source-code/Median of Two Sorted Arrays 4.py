# 4. Median of Two Sorted Arrays


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
        
            
            
            
                
        
        
        
        
        