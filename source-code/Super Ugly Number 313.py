# 313. Super Ugly Number
# ttungl@gmail.com

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # runtime: 535ms
        ugly = [1]*n
        i = [-1]*len(primes)
        v = [1]*len(primes)
        k=0
        while k<n:
            ugly[k] = min(v)
            for j in range(len(primes)):
                if v[j]==ugly[k]:
                    i[j] += 1 
                    v[j] = ugly[i[j]]*primes[j]
            k+=1
        return ugly[-1]
            
        
        
