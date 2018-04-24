# 186. Reverse Words in a String II
# ttungl@gmail.com
class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        # the sky is blue -> blue is sky the.
        # in-place!!
        str.reverse()
        idx = 0
        # str = eulb si yks eht
        for i in range(len(str)):                   # 01234; 567; 891011; 121314
            if str[i]==" ":                         # i=4; i=7; i=11;
                str[idx:i] = reversed(str[idx:i])   # s[0:4]=blue; s[5:7]=is; s[8:11]; 
                # update index idx
                idx = i + 1                         # idx=5; idx=8; idx=12
        str[idx:]=reversed(str[idx:])               # last word. s[12:]=the.
