# 767. Reorganize String
# ttungl@gmail.com
# Given a string S, check if the letters can be rearranged so that 
# two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, 
# return the empty string.

# Example 1:
# Input: S = "aab"
# Output: "aba"

# Example 2:
# Input: S = "aaab"
# Output: ""

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # sol 1:
        # priority queue (heap)
        # runtime: 48ms
        res, heap = "", []
        c = collections.Counter(S) # count chars occurrence.
        [heapq.heappush(heap, (-v, k)) for k, v in c.items()] # push to heap.
        # heap = [(-2,a), (-1,b)]
        heapi, heapj = 0, "" # store index and char
        while heap: 
            i, j = heapq.heappop(heap) # (v,k): (i,j)=(-2,a); (-1,b); (-1,a);
            res += j # res=""+a; ab; aba;
            if heapi < 0: # if value < 0; hi=0; hi=-1; hi=0
                heapq.heappush(heap, (heapi, heapj)) # heap=[(-1,a)]
            i+=1 # i=-1; i=0; i=1
            heapi, heapj = i, j # hi=-1, hj=a; hi=0;hj=b; hi=0;hj=a
        return res if len(res)==len(S) else ""
        
        # sol 2:
        # use count and extend
        # runtime:
        # src: https://leetcode.com/articles/reorganized-string/
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)/2: return ""
            A.extend(c * x)
        ans = [None] * N
        ans[::2], ans[1::2] = A[N/2:], A[:N/2]
        return "".join(ans)




