# 94. Binary Tree Inorder Traversal


# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # sol 1:
        # DFS
        # runtime: 40ms
        def dfs(root):
            if root.left:
                dfs(root.left)
            res.append(root.val)
            if root.right:
                dfs(root.right)
        if not root:
            return []
        res = []
        dfs(root)
        return res
    
        # sol 2:
        # DFS-2
        # runtime: 36ms
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
        # sol 3:
        # BFS iterative
        # runtime: 45ms
        if not root:
            return []
        queue = [(root, False)]
        res = []
        while queue:
            node, visited = queue.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    queue.append((node.right, False))
                    queue.append((node, True))
                    queue.append((node.left, False))
        return res
    
        # sol 4
        # BFS iterative
        # runtime: 36ms
        if not root:
            return []
        queue, res = [], []
        while True:
            while root:
                queue.append(root)
                root = root.left
            if not queue:
                break
            node = queue.pop()
            res.append(node.val)
            root = node.right
        return res
        
        
            
            
            

