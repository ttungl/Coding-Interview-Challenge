# 669. Trim a Binary Search Tree
# ttungl@gmail.com
# Given a binary search tree and the lowest and highest boundaries as L and R, 
# trim the tree so that all its elements lies in [L, R] (R >= L). 
# You might need to change the root of the tree, so the result should return
# the new root of the trimmed binary search tree.


# Example 1:
# Input: 
#     1
#    / \
#   0   2

#   L = 1
#   R = 2

# Output: 
#     1
#       \
#        2


# Input: 
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1

#   L = 1
#   R = 3

# Output: 
#       3
#      / 
#    2   
#   /
#  1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # sol 1: recursive
        # runtime: 156ms
        if not root: return root
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        elif root.val < L: return self.trimBST(root.right, L, R)
        elif root.val > R: return self.trimBST(root.left, L, R)
        return root
    
        # sol 2:
        # runtime: 81ms
        if not root or R < L: return root
        if L > root.val: 
            return self.trimBST(root.right, L, R)
        elif R < root.val: 
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, root.val)
            root.right = self.trimBST(root.right, root.val, R)
            return root
    





