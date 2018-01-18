# 760. Find Anagram Mappings

# A = [12, 28, 46, 32, 50]
# B = [50, 12, 32, 46, 28]
# We should return
# [1, 4, 3, 2, 0]
# as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.
# Note:
# A, B have equal lengths in range [1, 100].
# A[i], B[i] are integers in range [0, 10^5].



class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # sol 1
        # time O(n) space O(n)
        # runtime: 36ms
        p, d = [], {}
        for i, v in enumerate(B): d[v] = i
        for v in A: p.append(d[v])
        return p

        # sol 2
        d = {b:i for i,b in enumerate(B)}
        return [d[a] for a in A]