# Implement Trie (Prefix Tree) 208
# ttungl@gmail.com
# Implement a trie with insert, search, and startsWith methods.
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

# Trie (we pronounce "try") or prefix tree is a tree data structure, 
# which is used for retrieval of a key in a dataset of strings. 
# There are various applications of this very efficient data structure 
# such as autocomplete, spellchecker, IP routing (longest prefix matching), 
# predictive text, solving word game, etc.
# src: https://leetcode.com/articles/implement-trie-prefix-tree/


class TrieNode(object):
    def __init__(self, k):
    	"""Initialize your data structure here."""
        self.children = {}
        self.v = 0

class Trie(object):        
    def __init__(self):
    	"""Initialize your data structure here."""
        self.root = TrieNode(None)

    def insert(self, word):
    	"""Inserts a word into the trie. :type word: [str] :rtype: [void] """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode(i)
            node = node.children[i]
        node.v +=1
        
    def beginsWith(self, prefix):
    	"""return trie or none if prefix or not"""
        node = self.root
        for i in prefix:
            if i in node.children:
                node = node.children[i]
            else:
                return None
        return node
        
    def search(self, word):
        """ Returns if the word is in the trie. :type word: [str] :rtype: [bool] """
        node = self.beginsWith(word)
        if node and node.v:
            return True
        else:
            return False
            
    def startsWith(self, prefix):
        """ Returns if there is any word in the trie that starts with the given prefix. :type prefix: str :rtype: bool """
        if self.beginsWith(prefix):
            return True
        else:
            return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)