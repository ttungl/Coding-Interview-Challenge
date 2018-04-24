# 140. Word Break II 140
# ttungl@gmail.com
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].

# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

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
        
        
        
        
        
        