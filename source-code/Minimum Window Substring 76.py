# Minimum Window Substring 76

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # solution
        # s[i:j] : current Window
        # s[L:R] : result Window
        # in forloop, add new char to window, if nothing's missing,
        # remove window start and update result.
        # runtime: 242ms
        need, miss = collections.Counter(t), len(t)
        i = L = R = 0
        for j, c in enumerate(s, 1): # start from 1.
            miss -= need[c] > 0 # miss : #chars missing
            need[c] -= 1 # need[c] : store #times needs for char c (>0).
            if miss==0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] +=1
                    i+=1
                if not R or j-i <= R-L: # update result if no missing.
                    L, R = i, j 
        return s[L:R]
    	
    	#########################################
        # sol 2:
        # time: O(n^2); space: O(n)
        # runtime: 132ms
        if not t: return ""
        map = [0 for _ in range(128)] # 8-bit chars.
        for i in t: map[ord(i)]+=1 # init the map
        begin = end = min_d = 0
        d = len(s)+2 # int_max
        count = len(t)
        
        while end < len(s):
            if map[ord(s[end])] > 0: 
            	count-=1
            map[ord(s[end])] -=1
            end +=1
            while count==0: # valid
                if end-begin < d: 
                    min_d = begin
                    d = end - begin
                map[ord(s[begin])]+=1
                if map[ord(s[begin])] > 0: 
                	count +=1 # make it valid
                begin +=1
        if d > len(s): return ""
        return s[min_d:(min_d+d)]
        
        
        
        
    
        
        
        
        
        