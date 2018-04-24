# 339. Nested List Weight Sum
# ttungl@gmail.com
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Example 1:
# Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

# Example 2:
# Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # sol 1:
        # iterative
        # runtime: 35ms
        res, depth = 0, 1
        while nestedList:
            res += depth * sum([i.getInteger() for i in nestedList if i.isInteger()])
            nestedList = sum([i.getList() for i in nestedList if not i.isInteger()], []) # flatten a list
            depth += 1
        return res
    
        # sol 2:
        # DFS recursive
        # runtime: 34ms
        def helperDFS(nestedList, depth):
            res = 0
            for i in nestedList:
                if i.isInteger():
                    res += depth * i.getInteger()
                else:
                    res += helperDFS(i.getList(), depth + 1)
            return res
        return helperDFS(nestedList, 1)
        
        
    
        
        
