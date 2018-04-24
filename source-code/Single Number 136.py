# 136. Single Number
# ttungl@gmail.com
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1
        # use dict
        # time O(n) space (n)
        # runtime: 49ms
        d = {}
        for i in nums:
            if i in d: d[i]+=1
            else: d[i]=1
        for i,v in d.items():
            if v==1: return i
        return 0
        
        # sol 2
        # XOR
        # time O(n) space O(1)
        # runtime: 45ms
        res = 0
        for n in nums:
            res ^= n
        return res