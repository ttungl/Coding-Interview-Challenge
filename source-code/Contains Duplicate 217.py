# 217. Contains Duplicate
# ttungl@gmail.com
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sol 1:
        # runtime: 75ms
        if not nums or len(nums)==1: 
            return False
        dic = collections.defaultdict(int)
        for i in nums:
            dic[i] += 1
        for i in dic.values(): 
            if i>=2: 
                return True
        return False
    
        # sol 2:
        # runtime: 45ms
        if nums == []:
            return False
        s = set(nums)
        return len(s) != len(nums)
        