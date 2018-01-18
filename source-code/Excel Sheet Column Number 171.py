# 171. Excel Sheet Column Number

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # almost!!!
        # strs = list(s)
        # if len(strs)==0: return 0
        # if len(strs)==1: return (ord(s)-64)
        # sums = ord(strs[0])-64
        # print(sums)
        # for i in range(len(s)):
        #     if i!=0:
        #         sums = 26**i + ord(strs[i])-64
        # # return sums
        # # print(sums)
        
        # sol 1: 26-base 
        # runtime: 39ms
        s = s[::-1] # reverse string CBA->ABC
        sums = 0
        for i, c in enumerate(s): # (i:c)=(0:A);(1:B);(2:C)
            x = (ord(c)-64) # x=1; x=2; x=3
            sums += (26**i)*x # sums= 1=(26^0)*1; s=53=1+(26^1)*2; s=2081=53+(26^2)*3
        return sums
        
        # sol 2:
        # runtime: 48ms
        # reduce(): for performing some computation on a list 
        # and returning the result. It applies a rolling computation 
        # to sequential pairs of values in a list.
        return reduce(lambda x,y: (26*x)+y, [ord(c)-64 for c in list(s)])
    
        
        
    
        
