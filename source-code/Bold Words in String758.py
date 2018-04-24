# 758. Bold Words in String
# ttungl@gmail.com
# given that words = ["ab", "bc"] and S = "aabcd", 
# we should return "a<b>abc</b>d". Note that returning 
# "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        # sol 1:
        # use array memo to memorize the bold words in string S.
        # time O(n^2) space O(n)
        # runtime: 72ms
        memo = [False]*len(S)
        for w in words:
            i = S.find(w)
            j = len(w)
            while i > -1:
                for x in range(i, i+j):
                    memo[x] = True 
                i = S.find(w, i+1) # i = -1 if not found.
                
        # retrieve the result from memo.
        res, i = [], 0
        while i < len(S):
            if memo[i]:
                res.append("<b>")
                while i < len(S) and memo[i]:
                    res.append(S[i])
                    i+=1
                res.append("</b>")
            else:
                res.append(S[i])
                i+=1
        return ''.join(res)


        # sol 2
        # use DP to store indexes of longest subsequence. 
        # runtime: 189ms
        dp = [0]*(len(S)+1)
        dp[len(S)] = len(S)
        for i in range(len(S)-1, -1, -1):
            submax = i
            for w in words:
                end = i + len(w)
                if S[i:end]== w:
                    submax = max(submax, end)
            temp = submax
            for j in range(i+1, submax+1):
                temp = max(temp, dp[j])
            dp[i] = temp
        
        res, i = "", 0
        while i < len(S):
            end = dp[i]
            if end==i:
                sub = S[i]
                end = i+1
            else:
                sub = "<b>{}</b>".format(S[i:end])
            res+=sub
            i=end
        return res
