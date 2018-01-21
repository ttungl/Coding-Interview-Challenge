# 264. Ugly Number II

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # sol 1:
        # runtime: 125ms
        # --
        ugly = [1]*n
        i2 = i3 = i5 = -1 # factor 
        v2 = v3 = v5 = 1 # value
        x = 1 # ugly number of n-th 
        for k in range(n):
            x = min(v2, v3, v5) 
            ugly[k] = x # update to the ugly array
            if x == v2: 
                i2 +=1; v2 = ugly[i2]*2
            if x == v3:
                i3 +=1; v3 = ugly[i3]*3
            if x == v5:
                i5 +=1; v5 = ugly[i5]*5
        return ugly[-1] # or x 
    
        # sol 2: optimized sol 1
        # runtime: 292ms
        # --
        ugly = [1]*n
        primes = [2,3,5]
        i = [-1]*3 # factor: for 2,3,5
        v = [1]*3 # value:
        k=0
        while k < n:
            ugly[k] = min(v)
            for j in range(3):
                if v[j] == ugly[k]:
                    i[j] += 1
                    v[j] = ugly[i[j]]*primes[j]
            k+=1
        return ugly[-1]
        
        # sol 3: priority queue
        # keep a heap to store a tuple (value, factor) 
        # to store the last factor the number was multiplied.
        # runtime: 298 ms
        # --
        heap = [(1,1)]
        primes = [2,3,5]
        for _ in range(n):
            val, fact = heapq.heappop(heap)
            for x in primes:
                if fact <= x:
                    heapq.heappush(heap, (val*x, x))
        return val
        
        
