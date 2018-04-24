# 694. Number of Distinct Islands
# ttungl@gmail.com


Use max area of Islands + count shapes.


def numDistintIslands(self, grid):

	def dfs(i, j, pos, nextPos):
		grid[i][j] = -1
		for d in ((-1,0),(1,0),(0,-1),(0,1)):
			x, y = i + d[0], j + d[1]
			if 0<= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]==1:
				next_pt = (nextPos[0] + d[0], nextPos[1] + d[1])
				pos.append(next_pt)
				dfs(x, y, pos, next_pt)

	res = set()
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				pos = []
				dfs(i, j, pos, (0, 0))
				res.add(tuple(pos))
	return len(res)



