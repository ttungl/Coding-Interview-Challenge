# 247. Strobogrammatic Number II
# ttungl@gmail.com
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Find all strobogrammatic numbers that are of length = n.

# For example,
# Given n = 2, return ["11","69","88","96"].


class Solution(object):
    
    # sol 1
    # runtime: 345ms
    def __init__(self):
        self.maps = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        c = ["#"]*n
        self.dfs(c, 0, n-1, res)
        return res
    
    def dfs(self, c, left, right, res):
        if left > right:
            s = ''.join(c)
            res.append(s)
            return
        for p in self.maps.iteritems():
            if left == right and p[0] in ('6', '9'):
                continue
            if left != right and left == 0 and p[0] == '0':
                continue
            c[left], c[right] = p[0], p[1]
            self.dfs(c, left + 1, right - 1, res)
                
    # sol 2:
    # runtime: 265ms
    def findStrobogrammatic(self, n):
        oddNum = ['0', '1', '8']
        evenNum = ['11', '88', '69', '96', '00']
        
        if n == 1:
            return oddNum
        if n == 2:
            return evenNum[:-1]
        if n % 2:
            pre, mid = self.findStrobogrammatic(n-1), oddNum
        else:
            pre, mid = self.findStrobogrammatic(n-2), evenNum
        premid = (n-1)/2
        return [p[:premid] + c + p[premid:] for c in mid for p in pre]
                
                



