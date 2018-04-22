# 820. Short Encoding of Words

# Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

# For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

# Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

# What is the length of the shortest reference string S possible that encodes the given words?

# Example:

# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: S = "time#bell#" and indexes = [0, 2, 5].
# Note:

# 1 <= words.length <= 2000.
# 1 <= words[i].length <= 7.
# Each word has only lowercase letters.


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # sol 1:
        # problem is converted to removing words that overlap
        # to words suffices and then lencount the rest of the set.
        # time O(n*m) space O(n)
        # runtime: 98ms
        s = set(words)
        for word in words:
            for i in range(1, len(word)): 
                s.discard(word[i:]) 
        return sum(len(word) + 1 for word in s)
    
    
        # sol 2:
        # runtime: 209ms
        d, leaves = dict(), []
        for word in set(words):
            cur = d
            for i in word[::-1]:
                cur[i] = cur = cur.get(i, dict())
            leaves.append((cur, len(word) + 1))
        return sum(depth for node, depth in leaves if len(node)==0)
    
        
        
    




