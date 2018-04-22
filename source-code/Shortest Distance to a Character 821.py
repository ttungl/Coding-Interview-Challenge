# 821. Shortest Distance to a Character

# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

# Note:

# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # sol 1:
        # runtime: 955ms
        return [min(abs(i - li) for li in [j for j,v in enumerate(S) if v==C]) for i in range(len(S))]
    
        # sol 2:
        # runtime:
        lst = [i for i,v in enumerate(S) if v==C]
        return [min(abs(i - j) for j in lst) for i in range(len(S))]
                
            

        # sol 2:
        # runtime: 62ms
        n = len(S)
        res = [n]*n
        pos = -n
        for i in range(n) + range(n)[::-1]:
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res


