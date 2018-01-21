# Top K Frequent Elements 347

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # use dictionary
        # runtime: 66ms
        d = {}
        for i in nums:
            if i in d: d[i] += 1
            else: d[i] = 1
        
        uniNums = sorted(d.keys())
        res = sorted(uniNums, key=lambda x: -d[x]) # descending order using -d[x], so only care from 0-k in res.
        return res[:k]
                