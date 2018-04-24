# 249. Group Shifted Strings
# ttungl@gmail.com
# https://leetcode.com/problems/group-shifted-strings/description/

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # sol 1
        # To identify each group, compute the modulo 26 difference between each letter in a word with the first letter in it.
        # time: O(n^2)
        # space: O(n)
        # runtime: 45ms
        d = {}
        for word in strings:
            key = tuple(map(lambda x: (ord(x) - ord(word[0]))%26, word)) # ord() method returns an integer.
            d[key] = d.get(key, []) + [word]
        return [sorted(x) for x in d.values()]
    
        # sol 2
        # To identify each group, compute the modulo 26 difference between each letter in a word with the first letter in it.
        # time: O(n*m)
        # space: O(n*m)
        # runtime: 45ms
        d = {}
        for word in strings:
            key = tuple((ord(c) - ord(word[0])) % 26 for c in word) # 
            d[key] = d.get(key, []) + [word]
        return [sorted(x) for x in d.values()]
        
    
        
