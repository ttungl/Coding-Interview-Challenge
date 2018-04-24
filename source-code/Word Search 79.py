# 79. Word Search
# ttungl@gmail.com

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # sol 1:
        # DFS
        # time O(n*m) space O(n)
        # runtime: 545ms
        def dfs(board, i, j, word, visited):
            if len(word) == 0: # hit base case
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited.get((i,j)) or word[0]!=board[i][j]:
                return False
            visited[(i,j)] = True
            res = dfs(board, i, j+1, word[1:], visited) \
                    or dfs(board, i+1, j, word[1:], visited) \
                    or dfs(board, i-1, j, word[1:], visited) \
                    or dfs(board, i, j-1, word[1:], visited)
            visited[(i,j)] = False
            return res
        if not board:
            return False
        visited = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word, visited):
                    return True
        return False
        
        
        # sol 2:
        # DFS
        # time O(n*m) space O(1)
        # runtime: 392ms
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and word[idx]==board[x][y]:
                    board[x][y] = '*'
                    if dfs(x, y, idx + 1):
                        return True
                    board[x][y] = word[idx]
            return False
            
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    board[i][j] = '*'
                    if dfs(i, j, 1):
                        return True
                    board[i][j] = word[0]
        return False
    
        
                        
            

        
    

        
   
        


