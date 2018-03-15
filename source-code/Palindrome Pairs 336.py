# 336. Palindrome Pairs


# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.




class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # sol 1:
        # time O(n*n) space O(n)
        # runtime: 900ms
        lookup = {w:i for i,w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                pre, pos = w[:j], w[j:]
                if pre==pre[::-1] and pos[::-1] != w \
                	and pos[::-1] in lookup:
                        res.append([lookup[pos[::-1]], i])
                if j != len(w) and pos==pos[::-1] \
                	and pre[::-1] != w and pre[::-1] in lookup:
                        res.append([i, lookup[pre[::-1]]])
        return res
    
    
        # sol 2:
        # runtime: 513ms
        lookup = {w[::-1]:i for i,w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                pre, pos = w[:j], w[j:]
                if pre in lookup and lookup[pre] != i and pos == pos[::-1]:
                    res.append([i, lookup[pre]])
                if j>0 and pos in lookup and lookup[pos] != i and pre == pre[::-1]:
                    res.append([lookup[pos], i])
        return res
        
        
        
                
            
            










        
        
                
            
            


