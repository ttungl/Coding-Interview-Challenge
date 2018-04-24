# // Valid Sudoku
# ttungl@gmail.com
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #########################################
        # sol1
        # check three constraints: row, column, and subsquare3x3 contain unique numbers from 1-9.
        # time complexity: O(n^2)
        # space complexity: O(n)
        visited = []
        for i, row in enumerate(board):
            for j, string in enumerate(row):
                if string != ".":
                    visited += (string,j), (i,string), (i/3, j/3, string) # use a tuple is faster than a list [].
        return len(visited) == len(set(visited))

        #########################################
        # sol2
        # time O(n^2)
        # space O(n)
        def is_valid_row(board):
            for row in board:
                if not is_valid(row):
                    return False
            return True
            
        def is_valid_column(board):
            for col in zip(*board): # zip(*board) gets the columns vector of a matrix.
                if not is_valid(col):
                    return False
            return True
            
        def is_valid_square(board):
            for i in (0,3,6):
                for j in (0,3,6):
                	square = [board[x][y] for x in range(i, i+3) 
                                          	for y in range(j, j+3)]
                    if not is_valid(square):
                        return False
            return True
        
        def is_valid(value):
            res = [i for i in value if i != '.'] # list comprehensions
            return len(res) == len(set(res))
        
        return is_valid_row(board) and is_valid_column(board) and is_valid_square(board)