# 106. Construct Binary Tree from Inorder and Postorder Traversal
# ttungl@gmail.com
# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7] # Left, Root, Right
# postorder = [9,15,7,20,3] # Left, Right, Root
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # sol 1:
        # use dict (val,idx) to keep track of the indices in both arrays.
        # runtime: 59ms
        def dfs(left, right):
            if left < right:
                node = TreeNode(postorder.pop()) # Left, right, root.
                index = dict[node.val]
                node.right = dfs(index + 1, right)
                node.left = dfs(left, index)
                return node
        dict = {v:i for i,v in enumerate(inorder)}
        return dfs(0, len(inorder))
        
        # sol 2
        # DFS using index
        # runtime: 194ms
        if inorder:
            idx = inorder.index(postorder.pop()) # Left, right, root.
            node = TreeNode(inorder[idx])
            node.right = self.buildTree(inorder[idx+1:], postorder)
            node.left = self.buildTree(inorder[:idx], postorder)
            return node
        
        
        
        
        
        
        
        
        





