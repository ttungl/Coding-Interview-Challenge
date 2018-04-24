# sudoku solver
# ttungl@gmail.com
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # sol 1:
        # desc.: 1/ create a dictionary "val" to keep all possible values in each cell/location.
        #        2/ for each time, choose one val from location with smallest possible values,
        #        then update the board with possible values from other locations/cells.
        #        If this val is valid, keep updating using DFS.
        #        If this val is invalid or infeasible, undo the updates and go back to select new val one.
        # time O(n^2)
        # space O(n)
        # note: related N-Queens problem.
        
        def possible_vals(board):
            a = "123456789"
            b, val = {}, {} 
            for i in xrange(9):
                for j in xrange(9):
                    cell = board[i][j] 
                    if cell !='.':
                        b[('r', i)] = b.get(('r',i), []) + [cell]
                        b[('c', j)] = b.get(('c',j), []) + [cell]
                        b[(i//3, j//3)] = b.get((i//3,j//3), []) + [cell]
                    else:
                        val[(i,j)] = []
            for (i,j) in val.keys():
                invalid = b.get(('r',i), []) + b.get(('c',j), []) + b.get((i//3,j//3), [])
                val[(i,j)] = [n for n in a if n not in invalid]
            return val
        
        def sdk_solver(val): # DFS 
            if len(val)==0: return True
            keep = min(val.keys(), key=lambda x: len(val[x]))
            nums = val[keep] 
            for i in nums: # check valid at each location, else undo the updates.
                update = {keep: val[keep]}
                if is_valid(val, i, keep, update): 
                    if sdk_solver(val): return True
                sdk_undo(val, keep, update)
            return False
        
        def is_valid(val, n, keep, update): # update if val is valid one.
            board[keep[0]][keep[1]] = n # update value
            del val[keep] # removes element "keep" in a dictionary "val"
            i,j = keep
            for idx in val.keys():
                if n in val[idx]:
                    if idx[0]==i or idx[1]==j or (idx[0]//3,idx[1]//3) == (i//3,j//3):
                        update[idx] = n
                        val[idx].remove(n)
                        if len(val[idx])==0: return False
                        
            return True
        
        def sdk_undo(val, keep, update): # backtracking
            board[keep[0]][keep[1]]='.' # update dot
            for k in update:
                if k not in val:
                    val[k] = update[k]
                else:
                    val[k].append(update[k])
            return None
        
        val = possible_vals(board)
        sdk_solver(val)
