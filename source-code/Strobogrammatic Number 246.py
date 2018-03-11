# 246. Strobogrammatic Number


# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to determine if a number is strobogrammatic. The number is represented as a string.

# For example, the numbers "69", "88", and "818" are all strobogrammatic.



class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # sol 1:
        # runtime: 40ms
        maps = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        l, r = 0, len(num) - 1
        if not num:
            return True     
        while (l <= r):
            if num[r] not in maps \
                or (maps[num[r]] != num[l]):
                return False
            l += 1
            r -= 1
        return True
    
        # sol 2
        # runtime: 42ms
        maps = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        if not num:
            return True
        n = len(num)
        for i in range(int(n/2)+1):
            if num[i] not in maps or maps[num[i]] != num[-i-1]:
                return False
        return True
        
        