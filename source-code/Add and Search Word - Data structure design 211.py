# 211. Add and Search Word - Data structure design
# ttungl@gmail.com

# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# For example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.

# runtime: 182ms

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict(list)
        

    def addWord(self, word): # insert
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            self.children[len(word)].append(word)
        
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        
        if '.' not in word:
            return word in self.children[len(word)]
        
        for c in self.children[len(word)]:
            for i, ch in enumerate(word):
                if ch != c[i] and ch != '.':
                    break
            else:
                return True
        return False
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)









