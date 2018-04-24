# 647. Palindromic Substrings
# ttungl@gmail.com
# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".



class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sol 1:
        # time O(n*m) space O(1)
        # runtime: 171ms
        def dfs(s, left, right):
            count = 0
            while left >=0 and right < len(s) and s[left]==s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        res = 0
        for i in range(len(s)):
            res += dfs(s, i, i) + dfs(s, i, i + 1) # odd and even indices.
        return res
    
        # sol 2:
        # DP-2D
        # runtime: 519ms
        res = 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)):
                dp[i][j] = s[i]==s[j] and ((j - i < 3) or dp[i+1][j-1])
                if dp[i][j]:
                    res += 1
        return res
        
        # sol 3:
        # runtime: 1254ms
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    res += 1
        return res
            
