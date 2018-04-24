# 686. Repeated String Match
# ttungl@gmail.com

# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

# For example, with A = "abcd" and B = "cdabcdab".

# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

# Note:
# The length of A and B will be between 1 and 10000.


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # sol 1
        # append A until its lenA >= B
        # check matched string.
        cnt, strA = 0, ""
        while len(strA) < len(B):
            strA += A
            cnt += 1
            if B in strA:
                return cnt
        strA += A
        if B in strA: 
        	return cnt + 1
        else: 
        	return -1
        