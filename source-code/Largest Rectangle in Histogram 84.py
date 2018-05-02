# 84. Largest Rectangle in Histogram
# ttungl@gmail.com

# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# Example:

# Input: [2,1,5,6,2,3]
# Output: 10

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # sol 1:
        # traverse the heights list
        # check if current height < height of last idx in stack, then update max area.
        # time O(n*n) space O(n)
        # runtime:
        if not heights: return 0
        res, stack = 0, [0]
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i-1-stack[-1]
                res = max(res, h*w)
            stack.append(i)
        return res
    


