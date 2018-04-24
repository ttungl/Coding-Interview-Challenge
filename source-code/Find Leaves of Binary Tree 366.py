# 366. Find Leaves of Binary Tree
# ttungl@gmail.com
# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

# Example:
# Given binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Returns [4, 5, 3], [2], [1].

# Explanation:
# 1. Removing the leaves [4, 5, 3] would result in this tree:

#           1
#          / 
#         2          

# 2. Now removing the leaf [2] would result in this tree:

#           1          

# 3. Now removing the leaf [1] would result in the empty tree:

#           []         

# Returns [4, 5, 3], [2], [1].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # sol 1:
        # recursive
        # use dict and get max depth of level  
        # runtime: 40ms
        def findLeavesHelper(res, root):
            if not root: 
                return 0
            left = findLeavesHelper(res, root.left)
            right = findLeavesHelper(res, root.right)
            level = max(left, right) + 1
            res[level] += root.val, # iterable object
            return level
        res = collections.defaultdict(list)
        findLeavesHelper(res, root)
        return [i for i in res.values()]
    
        # sol 2:
        # recursive (optimized)
        # find max depth on left and right.
        # runtime: 37ms
        def findLeavesHelper(root):
            if not root: 
                return 0
            level = 1 + max(findLeavesHelper(root.left), findLeavesHelper(root.right))
            res[level-1] += root.val,
            return level
        res = collections.defaultdict(list)
        findLeavesHelper(root)
        return [i for i in res.values()]
    


