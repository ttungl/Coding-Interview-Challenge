# 315. Count of Smaller Numbers After Self
# ttungl@gmail.com

# You are given an integer array nums and you have to return a new counts array. 
# The counts array has the property where counts[i] is the number of smaller elements
# to the right of nums[i].

# Example:

# Given nums = [5, 2, 6, 1]

# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sol 1:
        # time worst O(n^2); best O(n logn); space O(n)
        # runtime: 174ms
        res, sortArr = [], []
        for i in nums[::-1]: # O(n)
            res.append(bisect.bisect_left(sortArr, i)) 
            bisect.insort(sortArr, i) # best: O(logn); worst O(n)
        return res[::-1]
            
        # sol 2:
        # binary search
        # runtime: 240ms
        res, sortArr = [0]*len(nums), []
        for i in range(len(nums)):
            left, right = 0, len(sortArr)-1
            index = len(nums) - 1 - i
            while left <= right:
                mid = left + (right-left)//2
                if sortArr[mid] < nums[index]:
                    left = mid+1
                else:
                    right = mid-1
            bisect.insort(sortArr, nums[index])
            res[index] = left
        return res
            
            
            
            

