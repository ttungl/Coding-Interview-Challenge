# 156. Binary Tree Upside Down
# ttungl@gmail.com
# Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

# For example:
# Given a binary tree {1,2,3,4,5},
#     1
#    / \
#   2   3
#  / \
# 4   5
# return the root of the binary tree [4,5,2,#,#,3,1].
#    4
#   / \
#  5   2
#     / \
#    3   1  
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # sol 1:
        # DFS recursive
        # runtime: 44ms
        if not root or not root.left:
            return root
        
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.right, root.left.left = root, root.right
        root.left, root.right = None, None
        return newRoot
        
        
        # sol 2:
        # BFS iterative
        # runtime: 43ms
        if not root:
            return root
        
        rLeft, rRight = root.left, root.right
        root.left, root.right = None, None
        
        while rLeft: # update left and right children, form new root.
            newLeft, newRight = rLeft.left, rLeft.right
            rLeft.left, rLeft.right = rRight, root
            root = rLeft
            rLeft, rRight = newLeft, newRight
        
        return root
        
        










