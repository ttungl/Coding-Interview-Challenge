# 100. Same Tree
# ttungl@gmail.com
# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # sol 1:
        # recursive
        # runtime: 36ms
        if p and q:
            return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q
    
        # sol 2:
        # iterative
        # runtime: 42ms
        queue = [(p, q)]
        while queue:
            p, q = queue.pop()
            if not p and not q:
                continue
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            else:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True
    




