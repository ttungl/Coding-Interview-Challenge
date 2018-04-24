# 813. Largest Sum of Averages
# ttungl@gmail.com
# We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

# Note that our partition must use every number in A, and that scores are not necessarily integers.

# Example:
# Input: 
# A = [9,1,2,3,9]
# K = 3
# Output: 20
# Explanation: 
# The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned A into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
 

# Note:

# 1 <= A.length <= 100.
# 1 <= A[i] <= 10000.
# 1 <= K <= A.length.
# Answers within 10^-6 of the correct answer will be accepted as correct.


class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        # sol 1:
        # Dynamic Programming memo bottom-up
        # runtime: 801ms
        d = collections.defaultdict(float)
        def search(n, k):
            if (n, k) in d: return d[(n, k)]
            if k == 1: 
                d[(n,k)] = sum(A[:n])/float(n)
                return d[(n,k)]
            d[(n,k)] = cur = 0
            for i in range(1, n)[::-1]:
                cur += A[i]
                d[(n,k)] = max(d[(n,k)], search(i, k-1) + cur/float(n-i))
            return d[(n,k)]
        return search(len(A), K)
    
        # sol 2:
        # DP
        # runtime: 328ms
        d = collections.defaultdict(float)
        def search(n, k):
            if (n,k) in d: return d[(n,k)]
            if k == 1: 
                d[(n,k)] = sum(A[n:])/float(len(A)-n)
                return d[(n,k)]
            d[(n,k)] = cur = 0
            for i in range(n, len(A)-k+1):
                cur += A[i]
                d[(n,k)] = max(d[(n,k)], search(i+1, k-1) + cur/float(i-n+1))
            return d[(n,k)]
        return search(0, K)
        
        
        
        
            
        
            
