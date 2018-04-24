# 783. Minimum Distance Between BST Nodes
# ttungl@gmail.com
# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

# Example :

# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.

# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

#           4
#         /   \
#       2      6
#      / \    
#     1   3  

# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
# Note:

# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # sol 1:
        # inorder traversal BST
        # time O(n) space O(n)
        # runtime:
        def dfs(node, arr=[]):
            if node.left: dfs(node.left, arr)
            arr.append(node.val)
            if node.right: dfs(node.right, arr)
            return arr
        arr = dfs(root)
        return min([abs(i-j) for i,j in zip(arr, arr[1:])])
        
        # sol 2:
        
        
        
        