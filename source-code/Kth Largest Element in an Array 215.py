# 215. Kth Largest Element in an Array


# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.




class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # sol 1 
        # time O(n log n)
        return sorted(nums)[-k]
        
        # sol 2
        # time O(n+(n-k)logk)
        heap = [] # minheap
        for i in nums:
            heapq.heappush(heap, i)
        for j in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
    