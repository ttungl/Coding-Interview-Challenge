# 229. Majority Element II

# Given an integer array of size n, find all elements that 
# appear more than ⌊ n/3 ⌋ times. The algorithm should run in 
# linear time and in O(1) space.

class Solution(object):
    def majorityElement(self, nums):
        # sol 1
        # time O(n) space O(k)
        # runtime: 50ms
        if not nums: return []
        n, res = len(nums)//3, []
        setnums = set(nums) # if there's no repetition for all elements, space could take O(n)!! In general cases, space takes O(k).
        for i in setnums:
            if nums.count(i) > n: res.append(i)
        return res
        
