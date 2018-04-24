# N-ary Tree Postorder Traversal
# ttungl@gmail.com

# Given an n-ary tree, return the postorder traversal of its nodes' values.

# For example, given a 3-ary tree:

#      1
#    / | \
#   3  2  4
#  / \
# 5   6

# Return its postorder traversal as: [5,6,3,2,4,1].


# Note: Recursive solution is trivial, could you do it iteratively?




"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # def isLeaf(node):
        #     if not node.children:
        #         return True
        #     return False
        
        # sol 1:
        # DFS recursion
        # runtime: 310ms
        def dfs(root):
            if not root:
                return []
            for c in root.children:
                dfs(c)
            res.append(root.val)
            return res
        res = []
        return dfs(root)
    
        # sol 2:
        # BFS iterative
        # runtime: 214ms
        if not root:
            return []
        queue = [(root, False)]
        res = []
        while queue:
            node, visited = queue.pop()
            if visited:
                res.append(node.val)
            else:
                queue.append((node, True))
                for c in node.children[::-1]:
                    queue.append((c, False))
        return res
        
        
        
