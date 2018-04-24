# Longest Palindromic Subsequence 516
# ttungl@gmail.com
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use dictionary d = {}
        # find left and right indices of character c
        # find max of maxlen and 1 if i=j, else 2 + recursive(s[i+1:j])
        # update maxlen to d[s] and return it.
        # note: bbbab has palindromic subsequence is bbbb (~4); palindromic substring is bab (~3).
        # time O(n)
        # space O(n)
        d = {}
        def find_palindrome(s):
            if s not in d:
                maxLen = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c) # get left and right indices of char in s.
                    maxLen = max(maxLen, 1 if i==j 
                                 else 2 + find_palindrome(s[i+1:j])) # 2+ when left and right are not equal.  
                d[s] = maxLen
            return d[s]
        
        return find_palindrome(s)