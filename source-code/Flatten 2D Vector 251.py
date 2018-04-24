# 251. Flatten 2D Vector
# ttungl@gmail.com

# Implement an iterator to flatten a 2d vector.

# For example,
# Given 2d vector =

# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

class Vector2D(object):

	# sol 1:
    # use list
    # runtime: 69ms
    def __init__(self, vec2d):
        self.nums = []
        for v in vec2d[::-1]:
            self.nums += v[::-1]
        
    def next(self):
        return self.nums.pop()

    def hasNext(self):
        return len(self.nums) > 0





    # sol 2:
    # runtime: 70ms
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.rows, self.cols, self.vec2d = 0, 0, vec2d

    def next(self):
        """
        :rtype: int
        """
        self.cols += 1
        return self.vec2d[self.rows][self.cols-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.rows < len(self.vec2d) and self.cols >= len(self.vec2d[self.rows]): # depends on each rows, we get different num cols.
            self.rows, self.cols = self.rows+1, 0
        return self.rows < len(self.vec2d)
            
    

        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())