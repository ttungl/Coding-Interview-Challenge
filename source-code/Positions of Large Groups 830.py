# 830. Positions of Large Groups

# In a string S of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

# The final answer should be in lexicographic order.

 

# Example 1:

# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
# Example 2:

# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# Example 3:

# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        # sol 1:
        # time O(n^2) space O(n)
        # runtime: 70ms
        res, n = [], len(S)
        i = j = 0
        while i < n:
            while j < n and S[i]==S[j]: j += 1
            if j - i >= 3: res.append([i,j-1])
            i = j
        return res
    
        # sol 2:
        # time O(n^2) space O(n)
        # runtime: 75ms
        res, j, s = [], 0, S + '.'
        for i in range(len(s)):
            if s[i] != s[j]:
                if i-j >= 3: res.append([j, i-1])
                j = i
        return res
    
        
        
        
            
            
            
            