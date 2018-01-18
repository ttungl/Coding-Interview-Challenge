# Longest Palindromic Substring 5

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # loop for string length
        #   loop for pairs: 

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
    
