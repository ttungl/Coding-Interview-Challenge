# 102. Binary Tree Level Order Traversal
# ttungl@gmail.com
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
        # sol 1:
        # BFS iterative
        # runtime: 50ms
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            res.append([node.val if node else None for node in queue])
            queue = [leaf for q in queue for leaf in (q.left, q.right) if leaf]
        return res


        # sol 2:
        # BFS iterative
        # runtime: 45ms
        if not root:
            return []
        res = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            node, depth = queue.pop()
            res[depth].append(node.val)
            if node.right:
                queue.append((node.right, depth + 1))
            if node.left:
                queue.append((node.left, depth + 1))
        return res.values()


        










            