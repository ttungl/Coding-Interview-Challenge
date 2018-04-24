# 126. Word Ladder II
# ttungl@gmail.com
# Given two words (beginWord and endWord), and a dictionary's word list, 
# find all shortest transformation sequence(s) from beginWord to endWord, such that:
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is 
# not a transformed word.
# For example,
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # Note: list allows duplicates which ar ladder from different words. 
        # Its size is much larger than that of the set.
        
        # sol 1: Depth-First Search
        # time
        # runtime
        def recurse(wordList, cur, d = collections.defaultdict(list)):
            if not cur: 
                return cur

            if endWord in cur: 
                return [[endWord]]
            
            wordList -= cur # 
            nextCur = set() # set has smaller size than list.
            
            for w in cur:
                for c in string.ascii_lowercase: # 'a..z'
                    for i in range(len(beginWord)): # check for each char in beginWord
                        word = w[:i] + c + w[i + 1:] # only one char changes in word W
                        if word in wordList: # if this change is in wordList, add to dict and nextCur
                            d[word].append(w)
                            nextCur.add(word)
            return [[y] + x for x in recurse(wordList, nextCur, d) for y in d[x[0]]] # recursive for nextCur.
            
        return recurse(set(wordList), set([beginWord]))
        
        
        # sol 2: Breadth-First Search
        # time O(n^2) space O(n)
        # runtime: 148ms
        left, right, wordList = set([beginWord]), set([endWord]), set(wordList)
        D, pathLen = collections.defaultdict(list), 1
        if endWord not in wordList: 
            return []
        while left and right:
            if left & right:
                paths = [[beginWord]]
                for _ in range(pathLen - 1):
                    paths = [path + [x] for path in paths for x in D[path[-1]]]
                return [path for path in paths if path[-1] == endWord]

            cur = min(left, right, key=len)
            wordList -= cur
            nextCur = set()
            for W in cur:
                for i in range(len(beginWord)):
                    for l in string.ascii_lowercase:
                        word = W[:i] + l + W[i + 1:]
                        if word in wordList:
                            nextCur.add(word)
                            if cur is left:
                                D[W].append(word)
                            else:
                                D[word].append(W)
            if cur is left:
                left = nextCur
            else:
                right = nextCur
            pathLen += 1
        return []
            
            
        
        
        
            
            
            
            
            
        


