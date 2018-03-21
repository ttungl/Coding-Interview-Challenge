# 124. Binary Tree Maximum Path Sum

# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # sol 1:
        # DFS
        # runtime: 165ms
        self.res = -sys.maxsize
        def dfs(root):
            if not root:
                return 0
            left = max(0, dfs(root.left)) # postorder
            right = max(0, dfs(root.right))
            self.res = max(self.res, left + right + root.val) # left to right
            return max(left, right) + root.val
        #
        dfs(root)
        return self.res
    
                
            
        
    
    



