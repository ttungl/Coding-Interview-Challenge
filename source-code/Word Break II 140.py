# 140. Word Break II 140

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # sol 1:
        # use DFS backtracking
        # runtime: 49ms
        d = {'':['']}
        def DFS(s):
            if s not in d:
                d[s] = [word + (tail and ' '+tail) 
                        for word in wordDict 
                        if s.startswith(word) 
                        for tail in DFS(s[len(word):])]
            return d[s]
        return DFS(s)
    
        # sol 2: 
        # runtime: 235ms
        d = {len(s): ['']}
        def dynamic(i):
            if i not in d:
                d[i] = [s[i:j] + (tail and ' '+tail)
                       for j in range(i+1, len(s)+1)
                       if s[i:j] in wordDict 
                       for tail in dynamic(j) ]
            return d[i]
        return dynamic(0)
        
        
        
        
        
        