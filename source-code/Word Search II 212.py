# 212. Word Search II

# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# For example,
# Given words = ["oath","pea","eat","rain"] and board =

# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.



class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # sol 1:
        # use DFS and trie.
        # runtime: 568ms
        def dfs(board, i, j, trie, path, res):
            if '#' in trie:
                res.append(path)
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in trie:
                return
            tmp = board[i][j]
            board[i][j] = '@'
            [dfs(board, i+d[0], j+d[1], trie[tmp], path+tmp, res) for d in directions]
            board[i][j] = tmp
        ##    
        trie, res = {}, []
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, i, j, trie, '', res)
        return list(set(res))
    
    
# sol 2:
# runtime: 826ms
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(list)
        
class Solution(object):
    def __init__(self):
        self.directions = ((0,1),(0,-1),(1,0),(-1,0))
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.children['#'] = '#'
                
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # sol 1:
        # use DFS and trie.
        # runtime: 844ms
        res = []
        node = self.root
        for word in words:
            self.insert(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, node, '', res)
        return list(set(res))
    
    def dfs(self, board, i, j, node, path, res):
        if '#' in node.children:
            res.append(path)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return
        tmp = board[i][j]
        board[i][j] = '@'
        [self.dfs(board, i+d[0], j+d[1], node.children[tmp], path+tmp, res) for d in self.directions]
        board[i][j] = tmp
        ##  
    
        
    
        
    
        
            

        
            
            
        
            
            


