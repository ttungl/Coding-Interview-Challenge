# 107. Binary Tree Level Order Traversal II

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # sol 1:
        # BFS iterative
        # runtime: 48ms
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            vals = [node.val if node else None for node in queue]
            res.append(vals)
            queue = [leaf for q in queue for leaf in (q.left, q.right) if leaf]
        return res[::-1]
        
        # sol 2
        # BFS iterative
        # runtime: 47ms
        if not root:
            return []
        queue = [(root, 0)]
        res = collections.defaultdict(list)
        while queue:
            node, depth = queue.pop()
            res[depth].append(node.val)
            if node.right:
                queue.append((node.right, depth + 1))
            if node.left:
                queue.append((node.left, depth + 1))
        return res.values()[::-1]





