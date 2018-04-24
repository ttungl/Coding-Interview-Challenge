# 459. Repeated Substring Pattern 
# ttungl@gmail.com

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
# Example 1:
# Input: "abab"

# Output: True

# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"

# Output: False
# Example 3:
# Input: "abcabcabcabc"

# Output: True

# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # sol 1
        # runtime: 39ms
        return s in (s+s)[1:-1]
    
        # sol 2
        # repeated substring s[:index+1], where index = ss.find(s) 
        # runtime: 38ms
        if not s: return True
        ss = (s+s)[1:-1]
        return ss.find(s) != -1







