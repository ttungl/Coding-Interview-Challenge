# 733. Flood Fill

# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.



class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # use dfs if next cell within bounds or same color as source cell.
        # space O(1)
        # runtime: 93ms
        rows, cols, pix = len(image), len(image[0]), image[sr][sc]
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i, j):
            # check within bounds
            if not (0<=i<rows and 0<=j<cols) \
                    or image[i][j] != pix: 
                return
            
            # assign new color
            image[i][j] = newColor

            # explore adjacent neighbors
            for d in dir:
                dfs(i+d[0], j+d[1])
                
        if newColor != pix:    
            dfs(sr, sc)
        return image
        
        # sol 2
        # use dfs to check if 4 directions containing (sr,sc) value, 
        # replace by newColor.
        # space O(n)
        # runtime: 90ms
        rows, cols, pix = len(image), len(image[0]), image[sr][sc] 
        dir = ((-1,0),(1,0),(0,1),(0,-1))
        visited = set()

        def dfs(i, j):
            if (i,j) in visited: # hit the base case.
                return
            
            visited.add((i,j)) # visited=((1,1))

            # traverse neighbors
            for d in dir: # 4-dir
                x, y = i+d[0], j+d[1] # x,y =1+(-1), 1+0= 0,1
                
                if 0<= x < rows and 0<= y < cols and image[x][y] == pix:
                    image[x][y] = newColor
                    dfs(x,y)

        if newColor != pix: # color=2; pix=1
            image[sr][sc]=newColor
            dfs(sr, sc) # (1,1)
        return image


        # sol 3
        # BFS
        # time O(n^2) space O(n)
        # runtime: 88ms
        rows, cols = len(image), len(image[0])
        pixel = image[sr][sc]
        if newColor == pixel: return image
        
        dir = ((-1,0),(1,0),(0,-1),(0,1))

        image.append([-1]*len(image[0])) # add an additional row to image. 
        [i.append(-1) for i in image] # add an additional col to image.
        
        queue = [(sr, sc)]
        while queue:
            i, j = queue.pop()
            image[i][j]=newColor
            for d in dir: # traverse neighbors
                x, y = i+d[0], j+d[1]
                if image[x][y]==pixel:
                    queue.append((x,y))
        return [res[:-1] for res in image[:-1]]




























