# 42. Trapping Rain Water


# Given n non-negative integers representing an elevation map where the width 
# of each bar is 1, compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # sol 1
        # time O(n) space O(1)
        # runtime: 41ms
        n = len(height)
        if n==0: return 0
        l, r = 0, n-1
        p1, p2 = height[l], height[r]
        water = total = p1 + p2
        while l != r:
            if height[l] < height[r]:
                l+=1
                total += height[l]
                p1 = max(p1, height[l])
                water += p1
            else:
                r-=1
                total += height[r]
                p2 = max(p2, height[r])
                water += p2
        return water - total
    
        # sol 2:
        # time O(n) space O(1)
        # runtime: 38ms
        res, n = 0, len(height)
        l, r = 0, n-1
        pl, pr = 0, 0
        while l <= r:
            if pl < pr:
                if height[l] < pl: res+= pl - height[l]
                else: pl = height[l]
                l+=1
            else:
                if height[r] < pr: res+= pr - height[r]
                else: pr = height[r]
                r-=1
        return res



