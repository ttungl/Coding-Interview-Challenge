# 316. Remove Duplicate Letters

# Given a string which contains only lowercase letters, 
# remove duplicate letters so that every letter appear once and only once. 
# You must make sure your result is the smallest in lexicographical order among all possible results.

# Example:
# Given "bcabc"
# Return "abc"

# Given "cbacdcbc"
# Return "acdb"


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # sol 1:
        # use seen to check visited nodes.
        # use stack to check duplicates.
        # time O(n*m) space O(n)
        # runtime:
        seen, stack = set(), []
        for i,c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and stack[-1] in s[i:]:
                    j = stack.pop()
                    seen.remove(j)
                seen.add(c)
                stack.append(c)
        return ''.join(stack)


        # sol 2:
        # get list of last index of each character.
        # check if not duplicate, add to res.
        # time O(n*m) space O(n)
        # runtime: 48ms
        d = {v:i for i,v in enumerate(s)}
        res = ''
        for i,v in enumerate(s):
            if v not in res:
                while v < res[-1:] and i < d[res[-1]]:
                    res = res[:-1]
                res += v
        return res
    
        
        
        







