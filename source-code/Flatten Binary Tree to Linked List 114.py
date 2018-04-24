# 114. Flatten Binary Tree to Linked List
# ttungl@gmail.com
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # sol 1: iterative
        # time O(n) space O(n)
        # runtime: 42ms
        # --
        if not root: 
        	return root
        node = TreeNode(0)
        stack = [root]
        while stack:
            level = stack.pop()
            if level: # level, right, left
                node.right, node.left = level, None
                if level.right: stack.append(level.right)
                if level.left: stack.append(level.left)
            node = level # add level
         
        # sol 2: recursive
        # runtime: 39ms
        # --
        if not root: 
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left:
            tmp = root.right
            root.right = root.left
            root.left = None
            while root.right:
                root = root.right
            root.right = tmp
    
