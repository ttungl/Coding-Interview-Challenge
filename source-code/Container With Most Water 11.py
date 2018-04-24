# 11. Container With Most Water
# ttungl@gmail.com

# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # sol 1:
        # use two pointers Left and Right to keep track of the area calculation. 
        # keep track of max area.
        # runtime: 72ms
        res, left, right = 0, 0, len(height)-1
        while left < right:
            res = max(res, min(height[left], height[right])*(right - left))
            if height[left] < height[right]: left += 1
            else: right -= 1
        return res
    
    
        # sol 2:
        # use DP 1-d
        # runtime: 58ms
        l, r = 0, len(height) - 1
        res = [0]*len(height)
        while l < r:
            if height[l] <= height[r]:
                res[l] = height[l]*(r - l) 
                l += 1
            else:
                res[r] = height[r]*(r - l)
                r -= 1
        return max(res)
        
        
        
            
        