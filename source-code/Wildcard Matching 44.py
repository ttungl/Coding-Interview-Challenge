# 44. Wildcard Matching
# ttungl@gmail.com

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # sol : Dynamic programming
        # runtime: 365ms
        if len(p) - p.count('*') > len(s): 
            return False
        dp = [True] + [False]*len(s)
        
        for i in p:
            if i != '*':
                for j in reversed(range(len(s))):
                    dp[j+1] = dp[j] and (i==s[j] or i=='?')
            else:
                for j in range(1, len(s)+1):
                    dp[j] |= dp[j-1]
            
            dp[0] &= i=='*'
        return dp[-1]
        
        
