# 161. One Edit Distance
# ttungl@gmail.com
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # sol 1:
        # time O(n) space O(1)
        # runtime: 35ms
        if len(s) > len(t): 
            s, t = t, s
        
        for i in range(len(s)):
            if s[i]!=t[i]:
                if s[i:]==t[i+1:] or s[i+1:]==t[i+1:]: return True
                else: return False
        return len(t) - len(s) == 1



        # sol 2:
        # runtime: 38ms
        m, n = len(s), len(t)
        if abs(m-n)>1: 
            return False
        
        x = min(m,n)
        i = j = 0

        while i < x and s[i]==t[i]: 
            i+=1

        while j < x-i and s[~j]==t[~j]: 
            j+=1

        return max(m,n) - (i+j)==1
    
        # sol 3: recursive
        # runtime: 32ms
        m, n = len(s), len(t)
        if m>n: 
            return self.isOneEditDistance(t,s) # swap str length
        if (n-m)>1 or s==t: 
            return False
        for i in range(m): 
            if s[i]!=t[i]:
                return s[i+1:]==t[i+1:] or s[i:]==t[i+1:]   
        return True


        
        
