# Top K Frequent Elements 347
# ttungl@gmail.com
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # use dictionary
        # time O(n log n)
        # runtime: 66ms
        d = {}
        for i in nums:
            if i in d: 
                d[i] += 1
            else: 
                d[i] = 1
        # for i in nums: d[i] = d.get(i, 0) + 1
        uniNums = sorted(d.keys())
        res = sorted(uniNums, key=lambda x: -d[x]) # descending order using -d[x], so only care from 0-k in res.
        return res[:k]


        # optimized sol 1:
        # time O(n log n)
        # runtime: 56ms
        d = collections.defaultdict(int)
        for n in nums:
            d[n] = d.get(n, 0) + 1
        res = sorted(d, key=lambda x: -d[x])
        return res[:k]


        # sol2 
        # use priority queue
        # runtime: 65ms
        d = collections.defaultdict(int)
        for n in nums: d[n] += 1
        return nsmallest(k, d, key=lambda x: -d[x])
    
    
        # sol 3:
        # use Counter and most_common.
        # runtime: 63ms
        d = collections.Counter(nums)
        return zip(*d.most_common(k))[0] # (0: key, 1: val)

