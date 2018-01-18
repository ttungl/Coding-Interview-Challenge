# 733. Flood Fill


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
        
    


