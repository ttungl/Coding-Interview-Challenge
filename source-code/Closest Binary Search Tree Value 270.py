# 270. Closest Binary Search Tree Value
# ttungl@gmail.com
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        while root:
            closest = min((root.val, closest), key=lambda x: abs(target - x))
            root = root.left if root.val > target else root.right
        return closest