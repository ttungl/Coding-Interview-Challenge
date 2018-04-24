# N-ary Tree Find Maximum Depth 
# ttungl@gmail.com
# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# For example, given a 3-ary tree:


#      1
#    / | \
#   3  2  4
#  / \
# 5   6


# We should return its max depth, which is 3.

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
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # sol 1:
        # BFS iterative
        # runtime: 210ms
        if not root:
            return 0
        queue = [(root, 0)]
        res = collections.defaultdict(list)
        while queue:
            node, depth = queue.pop()
            res[depth].append(node.val)
            for c in node.children:
                queue.append((c, depth + 1))
        return 1 + max(res.keys())
    
        # sol 2:
        # DFS
        # runtime: 170ms
        def dfs(root):
            if not root:
                return 0
            for c in root.children:
                res += 1
                dfs(c)
            return res
        res = 0
        return dfs(root)
    
        
    
        






