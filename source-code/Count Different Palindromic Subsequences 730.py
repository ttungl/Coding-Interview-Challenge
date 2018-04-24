# 730. Count Different Palindromic Subsequences
# ttungl@gmail.com

# Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.

# A subsequence of a string S is obtained by deleting 0 or more characters from S.

# A sequence is palindromic if it is equal to the sequence reversed.

# Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

# Example 1:
# Input: 
# S = 'bccb'
# Output: 6
# Explanation: 
# The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.
# Example 2:
# Input: 
# S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# Output: 104860361
# Explanation: 
# There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
# Note:

# The length of S will be in the range [1, 1000].
# Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.

class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        # sol 1:
        # bottom-up Dynamic Programming
        # use memo to avoid repetitions, else store count%modulo to memo.
        # time O(n^2) space O(n)
        # runtime: 2944ms
        modulo = 10**9 + 7
        res = 0
        charSet = 'abcd'
        def DFS(start, end, memo = {}):

            if (start, end) in memo:
                return memo[(start, end)]
        
            count = 0
            s = S[start:end+1]

            for x in charSet:
                try:
                    i, j = s.index(x) + start, s.rindex(x) + start
                except:
                    continue
                    
                count += DFS(i+1, j-1, memo) + 2 if i!=j else 1
                
            memo[(start, end)] = count % modulo
            return memo[(start, end)]
        
        return DFS(0, len(S)-1)
        
        




