# 144. Binary Tree Preorder Traversal



# Given a binary tree, return the preorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # sol 1:
        # DFS:
        # runtime: 48ms
        def dfs(root, res):
            if root:
                res.append(root.val)
            if root.left: dfs(root.left, res)
            if root.right: dfs(root.right, res)
            return res
        if not root:
            return []
        res = []
        return dfs(root, res)
    
        # sol 2:
        # DFS-2
        # runtime: 43ms
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
        
        # sol 3:
        # BFS iterative
        # runtime: 39ms
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
                    queue.append((node.left, False))
                    queue.append((node, True))
        return res


        # sol 4:
        # BFS queue
        # time O(n) space O(n)
        # runtime: 33ms
        if not root:
            return []
        queue = [root]
        node, res = root, []
        while queue:
            res.append(node.val)
            if node.right:
                queue.append(node.right)
            node = node.left
            if not node and queue:
                node = queue.pop()
        return res
        





