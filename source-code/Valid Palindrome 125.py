# 125. Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # time O(n); space O(1)
        # runtime: 162 ms
        news = ["".join(c) for c in s.lower() if c.isalnum()]
        for i in range(len(news)):
            if news[i]!=news[len(news)-i-1]:
                return False
        return True
        
        # sol 2:
        # runtime 69ms
        res = [c for c in s.lower() if c.isalnum()]
        return res==res[::-1] # res[::-1] its a built in utility from python and its time complexity is O(n)
        
       	