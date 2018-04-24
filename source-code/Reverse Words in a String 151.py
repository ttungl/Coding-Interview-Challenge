# 151. Reverse Words in a String
# ttungl@gmail.com
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # sol 1: not use in the interview
        # reverse the string, then join with space.
        # time O(n) space O(n)
        # runtime: 31ms
        return " ".join(reversed(s.split()))
    
        # sol 2
        # reverse the string s, 
        # then loop to reverse each word.
        # time O(n), space O(n)
        # runtime 35ms
        s = s[::-1]
        res = ""
        for i, each in enumerate(s.split()):
            if i!=0: 
            	res += " " + each[::-1] 
            else: 
            	res += each[::-1]
        return res
        
        
        
        
        
            


