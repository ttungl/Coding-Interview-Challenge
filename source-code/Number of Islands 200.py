# 200. Number of Islands

class Solution(object):

	# sol 1: use dfs
	# runtime: 122ms
	# --
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        rows, cols, count = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1': 
                    count+=1
                    self.dfs(grid, i, j)
        return count
    def dfs(self, grid, i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != '1': 
            return
        if grid[i][j] == '1': 
            grid[i][j] = '#'
            self.dfs(grid, i+1,j)
            self.dfs(grid, i-1,j)
            self.dfs(grid, i,j-1)
            self.dfs(grid, i,j+1)
    


    # sol 2: use stack
    # runtime: 82ms
    # --
    def numIslands(self, grid):
	    if not grid: 
	    	return 0
	    rows, cols, count = len(grid), len(grid[0]), 0
	    for i in range(rows):
	        for j in range(cols):
	            if grid[i][j]=="0":
	                continue
	            else:
	                count +=1
	                stack = []
	                stack.append([i,j])
	                # 
	                while len(stack) !=0:
	                    [x, y] = stack.pop()
	                    
	                    if x >= 1 and grid[x-1][y]=="1": 
	                        stack.append([x-1, y])
	                    if x < rows-1 and grid[x+1][y]=="1": 
	                        stack.append([x+1, y])
	                        
	                    if y >= 1 and grid[x][y-1]=="1": 
	                        stack.append([x, y-1])
	                    if y < cols-1 and grid[x][y+1]=="1": 
	                        stack.append([x, y+1])
	                    # update cell
	                    grid[x][y] = "0"
	    return count

