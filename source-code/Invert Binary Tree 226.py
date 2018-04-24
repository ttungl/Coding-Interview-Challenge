# 226. Invert Binary Tree
# ttungl@gmail.com
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # sol 1: recursive
        # runtime: 25ms
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        
        # sol 2: iterative
        # time: O(log n) space O(log n)
        # runtime: 32ms
        stack = [root]
        while stack:
            level = stack.pop()
            if level:
                level.left, level.right = level.right, level.left
                stack += level.left, level.right
        return root
    
        
        # sol 3: iterative
        # runtime: 32ms
        stack = [root]
        while stack:
            level = stack.pop()
            if level:
                level.left, level.right = level.right, level.left
                if level.left: stack.append(level.left)
                if level.right: stack.append(level.right)
        return root