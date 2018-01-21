# 1. Two Sum

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # sol 1:
        # runtime: 29ms
        d = {}
        for i, num in enumerate(nums):
            x = target - num # remaining number
            if x in d: # check if it's in dictionary to return its index and current index. Otherwise, adding i to num dictionary.
                return d[x], i 
            d[num]=i 
            
        # sol 2:
        # runtime: 39ms
        # [3,2,4] target=6
        d = {}
        for i, num in enumerate(nums): # (0,3);(1,2);(2,4) 
            if num in d: # 3!d; 2!d; 4:d
                return [d[num], i] # [d[4]=1,2]
            else: 
                d[target-num] = i # d[3 =6-3]=0; d[4=6-2]=1
        
        
        
        
            
        
        
            