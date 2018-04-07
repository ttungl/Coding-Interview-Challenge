# 279. Perfect Squares


# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # sol 1:
        # math
        # runtime: 43ms
        if n == 0: return 0
        while n%4 == 0: n/=4
        while n%9 == 0: n/=9
        while n%25 == 0: n/=25
        if n%8 == 7: return 4
        maxn = int(n**0.5)
        if maxn*maxn == n:
            return 1
        for i in range(1, maxn + 1):
            j = int((n-i*i)**0.5)
            if i*i + j*j == n: return 2
        return 3
        
        # sol 2:
        # BFS
        # runtime: 230ms
        if n < 2: return n
        
        # store squared nums <= n
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        # 
        res, lst = 0, {n}
        while lst:
            res += 1
            tem = set()
            for i in lst:
                for j in squares:
                    if i==j: return res
                    elif i < j: break
                    tem.add(i-j)
            lst = tem
        return res
        
        # sol 3:
        # DP
        # runtime: 3161ms
        dp = [0]
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[-1]





        
