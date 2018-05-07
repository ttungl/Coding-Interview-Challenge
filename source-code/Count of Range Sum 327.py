# 327. Count of Range Sum
# ttungl@gmail.com

# Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

# Note:
# A naive algorithm of O(n2) is trivial. You MUST do better than that.

# Example:
# Given nums = [-2, 5, -1], lower = -2, upper = 2,
# Return 3.
# The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
        # sol 1:
        # runtime: 116ms
        # from bisect import bisect_left, bisect_right
        if not nums: 
        	return 0
        n = len(nums)
        nsum = [nums[0]]

        for i in range(1, n):
            nsum.append(nsum[-1]+nums[i])
        
        sortedSums, res = sorted(nsum), 0

        for i in range(len(nsum)):
            left = bisect_left(sortedSums, lower+(nsum[i-1] if i>0 else 0))
            right = bisect_right(sortedSums, upper+(nsum[i-1] if i>0 else 0))
            res += right - left
            sortedSums.pop(bisect_left(sortedSums, nsum[i]))
        return res
        
        
        # sol 2:
        # merge-sort
        # time O(n logn) space O(n)
        # runtime:
        if not nums: 
        	return 0

        n = len(nums)
        nsum = [nums[0]]

        for num in nums:
            nsum.append(nsum[-1] + num)
        
        sortedSum, res = sorted(nsum), 0
        
        def mergeSort(lo, hi):
            mid = lo + (hi-lo)//2
            if mid == lo: 
            	return 0
            
            count = mergeSort(lo, mid) + mergeSort(mid, hi)
            
            left = right = mid
            
            for num in nsum[lo:mid]:
                while left < hi and nsum[left]-num < lower: 
                	left+=1
                while right < hi and nsum[right]-num <= upper: 
                	right+=1
                count += right - left
                
            nsum[lo:hi] = sorted(nsum[lo:hi])
            return count
        
        return mergeSort(0, len(nsum))
        
        
        
        
        
        # sol 3
        # use Binary Indexed Tree, store sum to nodes.
        # time O(n logn) space O(n)
        # as count and update take O(log n) time.
        # runtime: 263ms
        from bisect import bisect_left, bisect_right
        n = len(nums)
        nsum, BIT = [0]*(n+1), [0]*(n+2)
        def count(x):
            Sum = 0
            while x:
                Sum += BIT[x]
                x -= (x & -x)
            return Sum

        def update(x):
            while x <= n+1:
                BIT[x] += 1
                x += (x & -x)

        for i in range(n):
            nsum[i+1] = nsum[i] + nums[i]
        sortedNums, res = sorted(nsum), 0

        for i in nsum:
            res += count(bisect_right(sortedNums, i - lower)) - count(bisect_left(sortedNums, i - upper))
            update(bisect_left(sortedNums, i) + 1) # BIT starts at index 1.
        return res
    
    
        
