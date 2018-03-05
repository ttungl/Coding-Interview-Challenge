# 792. Number of Matching Subsequences

# Given string S and a dictionary of words words, 
# find the number of words[i] that is a subsequence of S.

# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that 
# are a subsequence of S: "a", "acd", "ace".

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # sol 4
        # use dictionary to keep track of indices and chars.
        # use binary search (bisect_left(list, x) to find 
        # the value in list that >= x, then return it.)
        # runtime: 1160ms
        def isMatch(word, w_i, d_i):
            if w_i == len(word): 
                return True
            l = dict_idxs[word[w_i]] # get list of indices of word[i] in dict.
            
            if len(l) == 0 or d_i > l[-1]: # d_i keeps track of increasing index.
                return False

            i = l[bisect.bisect_left(l, d_i)] # return the leftmost value >= d_i.
            
            return isMatch(word, w_i + 1, i + 1)

        dict_idxs = collections.defaultdict(list)

        for i in range(len(S)):
            dict_idxs[S[i]].append(i)
        return sum(isMatch(word, 0, 0) for word in words)


        # sol 3:
        # runtime: 1603ms
        res = 0
        for w in words:
            idx = 0
            brk = 0
            for c in w:
                idx = S.find(c, idx) # find index of c in S.
                if idx == -1: # not found
                    brk = 1
                    break
                idx += 1
            if brk == 0:
                res += 1
        return res


        # sol 1:
        # runtime: TLE
        res = 0
        for w in words:
            i = j = 0
            while i < len(S) and j < len(w):
                if S[i] == w[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if len(w) == j:
                res += 1
        return res

        # sol 2:
        # runtime: TLE
        n = len(S)
        table = [[0 if i < n else -1 for _ in range(26)] for i in range(n + 1)]
        
        for i in range(n-1, -1, -1):
            for j in range(26):
                table[i][j] = table[i+1][j]
            table[i][ord(S[i]) - ord('a')] = i+1
        
        res = 0
        for w in words:
            j = 0
            b = 0
            for c in w:
                if table[j][ord(c) - ord('a')] > -1:
                    j = table[j][ord(c) - ord('a')]
                else:
                    b = 1
                    break
            if b==0:
                res += 1
        return res

        

        
                