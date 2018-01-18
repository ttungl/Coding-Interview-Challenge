# 91. Decode Ways

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sol 1:
        # runtime: 58ms
        if s == "": return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            # dp[i]=dp[i-1] if s[i]!="0" + dp[i-2] if "09" < s[i-1:i+1]<"27".
            if i!=1 and s[i-2:i] < "27" and s[i-2:i] > "09":
                dp[i] += dp[i-2]
        return dp[len(s)]
    	
        # sol 2:
        # runtime: 35ms
        if len(s) == 0 or s[0] == '0': return 0
        dp = [0]*(len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s)+1):
            if s[i-1] > '0':
                dp[i] = dp[i-1]
            if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '7'):
                dp[i] += dp[i-2]
        return dp[len(s)]
        

        