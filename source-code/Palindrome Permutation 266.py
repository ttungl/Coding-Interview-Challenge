# 266. Palindrome Permutation

# sol
# Count the odd number in dictionary (s.count(i)%2==1: cnt++)
# If this odd number >1, then not palindrome, otherwise. 

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        Use dictionary<char, int> 
        Count the odd number in dictionary, 
        if this odd number > 1, then it's not palindrome, otherwise. 
        Time complexity: O(n); space O(n);
        Runtime: 35ms
        """
        # sol 1:
        # runtime: 32ms
        d = dict()
        cnt=0
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] +=1
        for c in s:
            if d.get(c)%2==1:
                d[c]=0
                cnt+=1
        return cnt<=1
    
        # sol 2:
        # runtime 39ms
        d, cnt = {}, 0
        for c in s:
            if c in d: d[c]+=1
            else: d[c]=1
        for c in s:
            if d.get(c) %2==1: d[c]=0; cnt+=1 
        return cnt<=1
    
        # sol 3:
        # runtime: 28ms
        # s=[abb]
        cnt = 0
        for i in set(s): # set=[a,b]
            if s.count(i)%2==1: # s.count(i): counts #times of i in list s.
                cnt+=1 
        return cnt<=1
        
                
        
        
                
        
