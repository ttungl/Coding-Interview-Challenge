# Group Anagrams
# ttungl@gmail.com
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # sol 1
        # time: O(m*n)
        # space: O(n*m)
        # runtime: 222ms
        d = {}
        for word in strs:
            key = tuple(sorted(word)) # use tuple to separate a string into characters.
            d[key] = d.get(key, []) + [word] # d.get(key, []) returns value to a given key.
        return d.values() # new view of the dictionary’s values.
        
        # sol 2
        # time: O(n*m)
        # space: O(n*m)
        # runtime: 218ms
        d = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in d:
                d.get(key).append(word)
            else:
                d[key] = [word]
        return d.values() # new view of the dictionary’s values
