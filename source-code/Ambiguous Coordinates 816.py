# 816. Ambiguous Coordinates

# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

# Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

# The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

# Example 1:
# Input: "(123)"
# Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
# Example 2:
# Input: "(00011)"
# Output:  ["(0.001, 1)", "(0, 0.011)"]
# Explanation: 
# 0.0, 00, 0001 or 00.01 are not allowed.
# Example 3:
# Input: "(0123)"
# Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
# Example 4:
# Input: "(100)"
# Output: [(10, 0)]
# Explanation: 
# 1.0 is not allowed.
 

# Note:

# 4 <= S.length <= 12.
# S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.
#  

class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # sol 1:
        # split the string into two parts. 
        # find all possibilities in each of two to form the valid coordinates.
        # corner cases: 
        # empty S; its first and last digits = 0: return []; 
        # if only last digit = 0: return [S]
        # if only first digit = 0: return adding dot to this string.
        # return the string 
        # runtime: 135ms
        S = S[1:-1] # remove brackets.
        def f(S):
            if not S or (len(S) > 1 and S[0] == S[-1] == '0'): return []
            if S[-1] == '0': return [S]
            if S[0] == '0': return [S[0] + '.' + S[1:]]
            return [S] + [S[:i] + '.' + S[i:] for i in range(1, len(S))]
        return ['(%s, %s)' % (a, b) for i in range(len(S)) 
                for a in f(S[:i]) for b in f(S[i:])] # alternative: itertools.product(f(S[:i]), f(S[i:])
    
        
