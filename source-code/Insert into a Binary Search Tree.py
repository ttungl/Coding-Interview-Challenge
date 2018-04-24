# Insert into a Binary Search Tree
# ttungl@gmail.com
# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# For example, 

# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:

#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# This tree is also valid:

#          5
#        /   \
#       2     7
#      / \   
#     1   3
#          \
#           4



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # sol 1:
        # runtime: 204ms
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root
    
        # sol 2:
        # runtime: 181ms
        if not root:
            return TreeNode(val)
        node = root
        while root:
            if root.val < val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    return node
            else:
                if root.left: 
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    return node
        
                
                
        