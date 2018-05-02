# 187. Repeated DNA Sequences
# ttungl@gmail.com


# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# For example,

# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # sol 1:
        # use dict to store pattern (k=10) and its count in the string.
        # time O(n) space O(n)
        # runtime: 215ms
        k = 10
        if len(s) < k: return []
        d = collections.defaultdict(int)
        for i in range(len(s)-k+1): 
            d[s[i:i+k]] += 1
        return [substr for substr, cnt in d.items() if cnt > 1]
    
        # sol 2:
        # use hashset to check overlapping substring.
        # time O(n) space O(n)
        # runtime: 132ms
        hset, res, k = set(), set(), 10
        for i in range(len(s)-k+1):
            sub = s[i:i+k]
            if sub in hset: res.add(sub)
            else: hset.add(sub)
        return list(res) 
            
        
