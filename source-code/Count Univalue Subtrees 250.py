# 250. Count Univalue Subtrees
# ttungl@gmail.com
# Given a binary tree, count the number of uni-value subtrees.

# A Uni-value subtree means all nodes of the subtree have the same value.

# For example:
# Given binary tree,
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
# return 4.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # sol 1:
        # DFS
        # runtime: 85ms
        self.cnt = 0
        def dfs(root):
            if not root:
                return True
            left, right = dfs(root.left), dfs(root.right) # postorder.
            if left and right:
                if root.left and root.left.val != root.val:
                    return False
                if root.right and root.right.val != root.val:
                    return False
                self.cnt += 1
                return True
            return False
        #
        if not root:
            return 0
        dfs(root)
        return self.cnt
    