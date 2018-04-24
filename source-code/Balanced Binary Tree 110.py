# 110. Balanced Binary Tree
# ttungl@gmail.com

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example 1:

# Given the following tree [3,9,20,null,null,15,7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:

# Given the following tree [1,2,2,3,3,null,null,4,4]:

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # sol 1
        # DFS
        # runtime: 79ms
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return 1 + max(left,right)
        return dfs(root) != -1
    
        # sol 2:
        # BFS iterative
        # runtime: 68ms
        stack, node = [], root
        last, depths = None, collections.defaultdict(int)
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths[node.left], depths[node.right]
                    if abs(left - right) > 1: 
                        return False
                    depths[node] = 1 + max(left, right)
                    last, node = node, None
                else:
                    node = node.right
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            






