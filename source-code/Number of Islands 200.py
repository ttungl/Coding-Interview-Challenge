# 200. Number of Islands
# ttungl@gmail.com

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011
# Answer: 3

class Solution(object):

	# sol 1: use dfs
	# runtime: 122ms
	# --
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: 
        	return 0
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
    

		# sol 3:
	    # DFS
	    # runtime: 117ms
	    def dfs(grid, i, j):
	        if 0 <= i < len(grid) and 0<= j <len(grid[0]) and grid[i][j] == '1':
	            grid[i][j] = '#'
	            dfs(grid, i+1, j)
	            dfs(grid, i-1, j)
	            dfs(grid, i, j-1)
	            dfs(grid, i, j+1)
	    if not grid:
	        return 0
	    rows, cols = len(grid), len(grid[0])
	    count = 0
	    for i in range(rows):
	        for j in range(cols):
	            if grid[i][j]=='1':
	                count += 1
	                dfs(grid, i, j)
	    return count
	


    # sol 2: use stack
    # runtime: 82ms
    # --
    def numIslands(self, grid):
	    if not grid: 
	    	return 0
	    rows, cols, count = len(grid), len(grid[0]), 0
	    for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    continue
                else:
                    count +=1
                    stack = []
                    stack.append([i,j])
                    while stack:
                        x, y = stack.pop()
                        if x > 0 and grid[x-1][y]=="1":
                            stack.append([x-1,y])
                        if x < rows-1 and grid[x+1][y]=="1":
                            stack.append([x+1, y])
                        if y > 0 and grid[x][y-1]=="1":
                            stack.append([x, y-1])
                        if y < cols-1 and grid[x][y+1]=="1":
                            stack.append([x, y+1])
                        grid[x][y] = "0"
        return count


