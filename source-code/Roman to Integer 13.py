# 13. Roman to Integer
# ttungl@gmail.com
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        res = 0
        # "MCMXCVI"
        for i in range(len(s)-1): # i=M;
            if d[s[i]] < d[s[i+1]]: #  
                res -= d[s[i]]
            else: 
                res += d[s[i]] # res+=1000;
        return res+d[s[-1]]
        

# 12. Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 123
        # sol 1:
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res, i = "", 0
        while num: 
            res += (num//values[i]) * numerals[i] # res+=(123//1000)*M; res+=(123//900)*M; ..; 
            num %= values[i] # num=123=123%1000; num=123=123%900; num=123=123%500; ..; 
            i += 1
        return res
