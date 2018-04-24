# 220. Contains Duplicate III
# ttungl@gmail.com
# Given an array of integers, find out whether there are two distinct indices i and j 
# in the array such that the absolute difference between nums[i] and nums[j] is 
# at most t and the absolute difference between i and j is at most k.


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # sol 1:
        # time O(n) space O(n)
        # runtime: 60ms
        if k < 1 or t < 0:
            return False

        d = collections.defaultdict()

        for i in range(len(nums)):
            key = nums[i]//(t+1) # shrink n toward zero.
            
            for h in (key, key-1, key+1):
                if h in d and abs(i - d[h][0]) <= k and abs(nums[i] - d[h][1]) <= t:
                    return True
            d[key] = (i, nums[i])
        return False

        # sol 2:
        # time O(n^2) space O(1)
        # runtime: 37ms
        if k < 1 or (t == 0 and k == 10000):
            return False
        for i in range(0, len(nums)):
            for j in range(i, min(i + 1 + k, len(nums))):
                if i == j:
                    continue
                if abs(i - j) <= k and abs(nums[i] - nums[j]) <= t:
                    return True
        return False