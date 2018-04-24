# Symmetric Tree 101.py
# ttungl@gmail.com
# Given a binary tree, check whether it is a mirror of itself 
# (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # sol 1:
        # DFS
        # time O(n) space O(log n)
        # runtime: 49ms
        def dfs(L, R):
            if L and R and L.val==R.val:
                return dfs(L.left, R.right) and dfs(L.right, R.left)
            return L==R
        if not root: return True
        return dfs(root.left, root.right)
    
    
        # sol 2
        # BFS
        # runtime: 44ms
        queue = [root]
        while queue: # q=1
            values = [i.val if i else None for i in queue]
            if values != values[::-1]: # check if sequence and its reversed one are different
                return False 
            queue = [c for i in queue if i for c in (i.left, i.right)]
        return True
            

        # sol 3
        # BFS
        # runtime: 42ms
        if root is None: 
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None: 
                continue
            elif left is None or right is None: 
                return False
            elif left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
        
        
        
        
        
        
        
        

