# 102. Binary Tree Level Order Traversal

# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # runtime: 45ms
        res, level = [], [root]
        while level and root:
            res.append([node.val for node in level])
            level = [leaf for x in level
                            for leaf in (x.left, x.right)
                                if leaf]
        return res
            