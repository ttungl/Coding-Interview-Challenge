# 235. Lowest Common Ancestor of a Binary Search Tree
# ttungl@gmail.com
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # sol 1:
        # DFS
        # runtime: 150ms
        if not root or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        elif left: return left
        elif right: return right
        
        # sol 2:
        # DFS
        # runtime: 115ms
        while root:
            if min(p.val, q.val) > root.val:
                root = root.right
            elif max(p.val, q.val) < root.val:
                root = root.left
            else:
                return root
        return None
        
        
        # sol 3:
        # BFS iterative
        # runtime: 117ms
        minval, maxval = min(p.val, q.val), max(p.val, q.val)
        while root:
            if minval > root.val:
                root = root.right
            elif maxval < root.val:
                root = root.left
            else:
                return root
        return None        
        
        
        
