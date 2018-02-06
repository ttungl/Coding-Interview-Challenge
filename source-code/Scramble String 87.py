# 87. Scramble String

# We say that "rgtae" is a scrambled string of "great".
# Given two strings s1 and s2 of the same length, 
# determine if s2 is a scrambled string of s1.

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # sol 1:
        # time O(n^2) space O(n)
        # runtime: 71ms
        def dfs(s1, s2):
            if s1 == s2: return True
            D, n = {}, len(s1)
            for i in range(n):
                D[s1[i]] = D[s1[i]] + 1 if s1[i] in D else 1
                D[s2[i]] = D[s2[i]] - 1 if s2[i] in D else -1
            for j in D:
                if D[j] != 0: return False
            for i in range(1, n): # partitioning
                if (dfs(s1[:i], s2[:i]) and dfs(s1[-(n-i):], s2[-(n-i):])) or (dfs(s1[:i], s2[-i:]) and dfs(s1[-(n-i):], s2[:(n-i)])):
                    return True
            return False

        return dfs(s1, s2)

        # sol 2
        # time O(n^2) space O(n)
        # runtime 63ms
        if s1==s2: return True
        
        if sorted(s1) !=sorted(s2): return False
        
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])): 
            	return True
        return False

