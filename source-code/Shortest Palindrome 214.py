# 214. Shortest Palindrome
# ttungl@gmail.com

# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

# For example:

# Given "aacecaaa", return "aaacecaaa".

# Given "abcd", return "dcbabcd".

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # sol 1:
        # use recursion and a pointer to find the index formed palindrome.
        # runtime: 89ms
        if not s or len(s)==1:
            return s
        j = 0
        for i in range(len(s))[::-1]:
            if s[i] == s[j]:
                j += 1
        # prefix + recursive + suffix
        return s[::-1][:len(s)-j] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):] 
    
        # sol 2
        # trick: s+"*"+s[::-1]
        # then using a lookup table in KMP to find palindrome length of substring. 
        # runtime: 89ms
        A = s + "*" + s[::-1]
        lookup = [0]
        for i in range(1, len(A)):
            index = lookup[i - 1]
            while(index > 0 and A[index] != A[i]):
                index = lookup[index - 1]
            lookup.append(index + (1 if A[index] == A[i] else 0))
        return s[lookup[-1]:][::-1] + s 
    
    
    
    
    
