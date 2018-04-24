# 425. Word Squares
# ttungl@gmail.com
# Given a set of words (without duplicates), find all word squares you can build from them.

# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

# b a l l
# a r e a
# l e a d
# l a d y

# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:

# Input:
# ["area","lead","wall","lady","ball"]

# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Example 2:

# Input:
# ["abat","baba","atan","atal"]

# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

class Solution(object):
    
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        # sol 1:
        # DFS
        # runtime: 811ms
        n = len(words[0])
        fulls = collections.defaultdict(list) # Trie.
        #
        for word in words:
            for i in range(n):
                fulls[word[:i]].append(word)
        #
        def buildSquare(square):
            if len(square) == n: # hit base case.
                squares.append(square)
                return
            [buildSquare(square + [word]) for word in fulls[''.join(zip(*square)[len(square)])]]
        #
        squares = []
        for word in words:
            buildSquare([word])
        return squares
    
##
# sol 2:
# Use Trie 
# runtime: 904ms
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(list)

class Solution(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, words):
        node = self.root
        for word in words:
            for i in range(len(words[0])):
                node.children[word[:i]].append(word)
    
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        def buildSquare(square):
            node = self.root
            if len(square) == len(words[0]):
                res.append(square)
                return
            for word in node.children[''.join(zip(*square)[len(square)])]:
                buildSquare(square + [word])
        
        res = []
        self.insert(words)
        for word in words:
            buildSquare([word])
        return res
                












