# 242. Valid Anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # sol 1:
        # runtime: 75 ms
        if len(s)!=len(t): return False
        dic1, dic2 = {}, {} 
        for i in s:
            dic1[i] = dic1.get(i, 0) + 1
        for i in t:
            dic2[i] = dic2.get(i, 0) + 1
        return dic1 == dic2
    
        
        # sol 2
        # runtime: 65 ms
        if len(s) != len(t): return False
        dic1, dic2 = [0]*26, [0]*26
        for i in s:
            dic1[ord(i)-ord('a')] += 1
        for i in t:
            dic2[ord(i)-ord('a')] += 1
        return dic1 == dic2
    

        # sol 3
        # runtime: 76 ms
        return sorted(s)==sorted(t)
    

        # sol 4
        # runtime: 56 ms
        dic = [0]*26 # 26 int arrays as buckets for each letter in alphabet
        for i in s:
            dic[ord(i)-ord('a')]+=1
        for i in t:
            dic[ord(i)-ord('a')]-=1
        for i in range(len(dic)):
            if dic[i]!=0:
                return False
        return True
        
        
        
        
        
        
            
