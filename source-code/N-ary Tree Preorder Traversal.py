# N-ary Tree Preorder Traversal

# Given an n-ary tree, return the preorder traversal of its nodes' values.


# For example, given a 3-ary tree:

#      1
#    / | \
#   3  2  4
#  / \
# 5   6


# Return its preorder traversal as: [1,3,5,6,2,4].

# Note: Recursive solution is trivial, could you do it iteratively?


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # sol 1:
		# DFS
		# runtime: 217ms
        def dfs(root):
            if not root:
                return []
            if root:
                res.append(root.val)
            if root.children:
                for c in root.children:
                    dfs(c)
            return res
        res = []
        return dfs(root)
    
        # sol 2:
        # BFS iterative
        # runtime: 205ms
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop()
            res.append(node.val)
            if node.children:
                for c in node.children[::-1]:
                    queue.append(c)
        return res
        
    
    
    
    
    
    
    
    








