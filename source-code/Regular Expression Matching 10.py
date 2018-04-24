# 10. Regular Expression Matching
# ttungl@gmail.com

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # sol 1: using an array
        # keep tracking on the prev array. 
        # runtime: 69 ms
        # --
        prev = [False, True]
        [prev.append(p[j]=='*' and prev[j]) for j in range(len(p))]
        
        for i in range(len(s)):
            cur = [False, False]
            for j in range(len(p)):
                if p[j]=='*':
                    cur.append(cur[j] or cur[j+1] or (prev[j+2] and p[j-1] in (s[i], '.')))
                else:
                    cur.append(prev[j+1] and p[j] in (s[i], '.'))
            # update
            prev = cur
        return prev[-1]
        
        # sol 2: Dynamic Programming
        # runtime: 69ms
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        
        dp[0][0] = True # init
        
        for i in range(1, len(p)):
            dp[i+1][0] = dp[i-1][0] and p[i]=='*'
        
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i]=='*':
                    dp[i+1][j+1] = dp[i-1][j+1] or dp[i][j+1]
                    if p[i-1]==s[j] or p[i-1]=='.':
                        dp[i+1][j+1] |= dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i][j] and (p[i]==s[j] or p[i]=='.')
        return dp[-1][-1]
                    
                    
            
        
        
        
        
        

