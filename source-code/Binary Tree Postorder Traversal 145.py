# 145. Binary Tree Postorder Traversal
# ttungl@gmail.com
# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],

#    1
#     \
#      2
#     /
#    3
 

# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # sol 1:
        # DFS recursive
        # runtime: 39ms
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
    
        # sol 2:
        # DFS-2
        # runtime: 40ms
        def dfs(root):
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            res.append(root.val)
        if not root:
            return []
        res = []
        dfs(root)
        return res
    
    
        # sol 3:
        # BFS iterative
        # runtime: 33ms
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
                    queue.append((node, True))
                    queue.append((node.right, False))
                    queue.append((node.left, False))
        return res
                
                
        
        
        





