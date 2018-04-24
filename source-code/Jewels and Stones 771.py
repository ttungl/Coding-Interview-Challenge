# 771. Jewels and Stones
# ttungl@gmail.com
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # store chars in S to dictionary
        # loop chars in J and count the types.
        # time O(n) space O(n)
        # runtime 52ms
        d, count ={}, 0
        for i in S:
            if i not in d: d[i]=1
            else: d[i]+=1
        for j in J:
            if j in d:
                count+=d[j]
        return count
    
        # sol 2:
        # runtime: 39ms
        Jset, count = set(J), 0
        for i in S:
            if i in Jset:
                count+=1
        return count
        
        # sol 3:
        # runtime: 36ms
        Jset = set(J)
        return sum([1 for i in S if i in Jset])
        
        
        
        
        