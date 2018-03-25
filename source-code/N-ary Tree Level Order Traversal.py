# N-ary Tree Level Order Traversal


# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example, given a 3-ary tree:

#      1
#    / | \
#   3  2  4
#  / \
# 5   6

# We should return its level order traversal:

# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
# Note:
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # sol 1:
        # BFS iterative
        # time O(n) space O(n)
        # runtime: 200ms
        if not root:
            return []
        queue = [(root, 0)]
        res = collections.defaultdict(list)
        while queue:
            node, depth = queue.pop()
            res[depth].append(node.val)
            for c in node.children[::-1]:
                queue.append((c, depth + 1))
        return res.values()
    
        # sol 2:
        # BFS
        # runtime: 210ms
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            res.append([node.val if node else None for node in queue])
            queue = [leaf for q in queue for leaf in q.children if leaf]
        return res
        
        