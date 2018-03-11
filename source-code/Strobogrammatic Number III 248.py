# 248. Strobogrammatic Number III

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

# For example,
# Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

# Note:
# Because the range might be a large number, the low and high numbers are represented as string.



class Solution(object):
    
    # sol 1
    # DFS
    # runtime: 802ms
    def __init__(self, res=0, low=0, high=0):
        self.res = res
        self.low = low
        self.high = high
        self.maps = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.low, self.high = low, high
        n, m = len(self.low), len(self.high)
        for i in range(n, m+1):
            c = ["#"]*i
            self.dfs(c, 0, i-1)
        return self.res
    
    def dfs(self, c, left, right):
        if left > right: # hit base
            s = "".join(c)
            if (len(s)==len(self.low) and int(s) < int(self.low)) \
                or (len(s)==len(self.high) and int(s) > int(self.high)):
                    return
            self.res += 1
            return

        for p in self.maps.iteritems():
            c[left], c[right] = p[0], p[1]
            if len(c) != 1 and c[0] == '0':
                continue
            if left < right or left == right and p[0]==p[1]:
                self.dfs(c, left + 1, right - 1)


    ###
    # sol 2
    # runtime:
    def __init__(self, res=0, low=0, high=0):
        self.res = res
        self.low = low
        self.high = high
        self.maps = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.low, self.high = low, high
        n, m = len(self.low), len(self.high)
        for i in range(n, m+1):
            c = ["#"]*i
            self.dfs(c, 0, i-1)
        return self.res
    
    def dfs(self, c, left, right):
        if left > right:
            s = "".join(c)
            if (len(s)==len(self.low) and int(s) < int(self.low)) \
                or (len(s)==len(self.high) and int(s) > int(self.high)):
                    return
            self.res += 1
            return
        
        for p in self.maps.iteritems():
            if left==right and p[0] in ['6', '9']:
                continue
            if left !=right and left==0 and p[0]=='0':
                continue
            c[left], c[right] = p[0], p[1]
            self.dfs(c, left + 1, right - 1)
    
    
    ###
    # sol 3:
    # runtime: 401ms
    def strobogrammaticInRange(self, low, high):
        lo, hi, ret = len(low), len(high), 0
        for i in range(lo, hi+1):
            vals = self.totalNum(i, i)
            lenVal = len(vals)
            if i == lo:
                for j in range(lenVal):
                    if int(vals[j]) < int(low):
                        lenVal -= 1
            if i == hi:
                for j in range(len(vals)):
                    if int(vals[j]) > int(high):
                        lenVal -= 1
            ret += lenVal
        return ret
    
    def totalNum(self, n, m):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']
            vals = self.totalNum(n - 2, m)
            res = []
            for val in vals:
                if m != n:
                    res.append('0' + val + '0')
                res.append('1' + val + '1')
                res.append('6' + val + '9')
                res.append('8' + val + '8')
                res.append('9' + val + '6')
            return res
    
    
    
    
    