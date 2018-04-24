# 775. Global and Local Inversions
# ttungl@gmail.com

# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

# Return true if and only if the number of global inversions is equal to the number of local inversions.

# Example 1:

# Input: A = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion, and 1 local inversion.
# Example 2:

# Input: A = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions, and 1 local inversion.
# Note:

# A will be a permutation of [0, 1, ..., A.length - 1].
# A will have length in range [1, 5000].
# The time limit for this problem has been reduced.


class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # sol 1: 
        # each number can't move more than 1 index.
        # (global = local) happens when each number i in [i-1, i+1]
        # Arrange an ideal permutation and found that to place number i,
		# only can place i at A[i-1],A[i] or A[i+1]. So, just check if 
		# all A[i] - i equals to -1, 0 or 1 (ideal permutation)
        # runtime: 93ms
        return all(False for i,v in enumerate(A) if abs(i-v) > 1)
    
        
        # sol 2:
        # if Global inversion == local inversions, 
		# Then all global inversion are local inversions.
		# if there is a global inversion that is not a local one, 
		# Then number of global inversion != local inversions.
        # runtime 122ms
        cmax = 0
        for i in range(len(A) - 2):
            cmax = max(cmax, A[i])
            if cmax > A[i + 2]: # can't find A[i] > A[j] with i+2<=j ~~ True if max(A[i]) < A[i+2]
                return False
        return True


        # sol 3:
        # runtime 180ms
        n = len(A)
        i, m = n-3, A[-1]
        while i >= 0:
            if A[i] > m:
                return False
            m = min(m,A[i+1])
            i -= 1
        return True



