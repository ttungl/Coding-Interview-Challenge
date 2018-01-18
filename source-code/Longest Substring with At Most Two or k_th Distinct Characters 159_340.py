# 159. Longest Substring with At Most Two Distinct Characters
# 340. Longest Substring with At Most K Distinct Characters

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # substring problems
        # 1. define map
        # 2. counter to check if substring is valid
        # 3. two pointers, one head and one tail
        # 4. define a length of substring
        # 5. Init a hashmap
        # 6. while loop for tail pointer < length of s.
            # check s[end++] in map[]--: counter--
            # while loop counter condition: update length of substring if finding minimum
            # increase begin to make it valid/invalid again
            # check s[begin++] in map[]++: counter++
        # 7. update d if maximum found.
        # 8. return 
        
        # runtime: 76ms
        map = [0 for _ in range(128)] # 8-bit 
        counter = 0
        begin = end = d = 0 # d: length of substring; counter: valid/invalid status; begin/end ~ head/tail; 
        while end < len(s):
            if map[ord(s[end])]==0: counter += 1
            map[ord(s[end])] += 1
            end += 1
            # counter condition
            while counter > 2: # Solution valid for kth distinct characters by replacing 2 by k.
                if map[ord(s[begin])] == 1: counter-=1
                map[ord(s[begin])]-=1
                begin +=1
            # update d if maximum found
            d = max(d, end-begin)
            
        return d


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # time 
        # runtime: 129ms
        map = [0 for _ in range(128)] # 8-bit 
        counter = 0
        begin = end = d = 0 # d: length of substring; counter: valid/invalid status; begin/end of string; 
        while end < len(s):
            if map[ord(s[end])]==0: counter += 1
            map[ord(s[end])] += 1
            end += 1
            # counter condition
            while counter > k: 
                if map[ord(s[begin])] == 1: counter-=1
                map[ord(s[begin])]-=1
                begin +=1
            # update d if maximum found
            d = max(d, end-begin)
        return d



