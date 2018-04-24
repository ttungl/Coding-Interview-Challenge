# 105. Construct Binary Tree from Preorder and Inorder Traversal
# ttungl@gmail.com

# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # sol 1:
        # runtime: 200ms
        if inorder:
            idx = inorder.index(preorder.pop(0)) # Root, left, right
            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx+1:])
            return node
        
        # sol 2
        # runtime:
        # use dict (val,idx) to keep track of the indices in both arrays.
        # runtime: 59ms
        def dfs(left, right):
            if left < right:
                node = TreeNode(preorder.pop(0)) # Root, left, right
                index = dict[node.val]
                node.left = dfs(left, index)
                node.right = dfs(index + 1, right)
                return node
        dict = {v:i for i,v in enumerate(inorder)}
        return dfs(0, len(inorder))
        
        
        
        
