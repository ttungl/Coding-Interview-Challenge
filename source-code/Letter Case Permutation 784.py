# 784. Letter Case Permutation


# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]
# Note:

# S will be a string with length at most 12.
# S will consist only of letters or digits.


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # sol 1:
        # runtime: 119ms
        res = ['']
        for ch in S:
            if ch.isalpha(): 
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else: 
                res = [i+ch for i in res]
        return res
            
        # sol 2:
        # runtime: 133ms
        Letters = [[i.upper(), i.lower()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*Letters)]
    
    
        
        