# 828. Unique Letter String

# A character is unique in string S if it occurs exactly once in it.

# For example, in string S = "LETTER", the only unique characters are "L" and "R".

# Let's define UNIQ(S) as the number of unique characters in string S.

# For example, UNIQ("LETTER") =  2.

# Given a string S, calculate the sum of UNIQ(substring) over all non-empty substrings of S.

# If there are two or more equal substrings at different positions in S, we consider them different.

# Since the answer can be very large, retrun the answer modulo 10 ^ 9 + 7.

 

# Example 1:

# Input: "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Evey substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
# Example 2:

# Input: "ABA"
# Output: 8
# Explanation: The same as example 1, except uni("ABA") = 1.
 

# Note: 0 <= S.length <= 10000.

class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        # sol 1:
        # # keep track of letters' indices.
        # runtime: 89ms
        res = 0
        d = {c: [-1,-1] for c in set(S)}
        for i, c in enumerate(S):
            k, j = d[c]
            d[c] = [j, i]
            res += (i-j)*(j-k)
        for c in d:
            k, j = d[c]
            res += (len(S)-j)*(j-k)
        return res 
        
        # sol 2:
        # keep track of letters' indices.
        # runtime: 131ms
        res = 0
        d = {c: [-1] for c in set(S)}
        for i, c in enumerate(S):
            d[c].append(i)
            if len(d[c]) >=3:
                k, j, i = d[c][-3], d[c][-2], d[c][-1]
                res += (i-j)*(j-k)
        for c in d:
            i, j = d[c][-1], d[c][-2]
            res += (len(S)-i)*(i-j)
        return res 
                
            