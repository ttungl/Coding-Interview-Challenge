# 217. Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums)==1: 
            return False
        dic = {}
        for i in nums:
            if i not in dic: dic[i] = 1
            else: dic[i] += 1 
        for i in dic.values(): 
            if i>=2: return True
        return False
        