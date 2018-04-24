# Longest Palindromic Substring 5
# ttungl@gmail.com
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.
 

# Example:

# Input: "cbbd"

# Output: "bb"
 



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # sol 1:
        # runtime:
        res = ""
        def helper(s, left, right):
            while left >=0 and right < len(s) and s[left]==s[right]:
                left-=1; right+=1
            return s[left+1:right]
            
        for i in range(len(s)):
            for j in range(2):
                temp = helper(s, i, i+j)
                if len(temp)>len(res): 
                    res=temp 
        return res

        # sol 2
        # runtime: 1591ms
        def dfs(s, i, j):
            while i >= 0 and j < len(s) and s[i]==s[j]:
                i-=1; j+=1
            return s[i+1:j]
        res = tem = ""
        for i in range(len(s)):
            for j in range(2):
                tem = dfs(s, i, i+j)
                res = tem if len(res) < len(tem) else res  
        return res  











    
