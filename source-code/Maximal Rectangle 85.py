# 85. Maximal Rectangle
# ttungl@gmail.com

# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example:

# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # sol 1:
        # find max of largest rectangle area for each height (in each row).
        # runtime: 153ms
        if not matrix: 
        	return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0]*(cols+1)
        res = 0
        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j]=='1' else 0
            
            stack = [0]
            for j in range(len(heights)):
                while stack and heights[stack[-1]] > heights[j]:
                    h = heights[stack.pop()]
                    w = j if not stack else j-1-stack[-1]
                    res = max(res, h*w)
                stack.append(j)
        
        return res
    
        # sol 2:
        # get heights of each row, compare max.
        # runtime: 138ms
        if not matrix or not matrix[0]: return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0]*(cols+1)
        res = 0
        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j]=='1' else 0
            res = max(res, self.largestRectArea(heights))
        return res

    def largestRectArea(self, heights):
        ans, stack = 0, [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i-1-stack[-1]
                ans = max(ans, h*w)
            stack.append(i)
        return ans
    
        




