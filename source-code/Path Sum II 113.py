# 113. Path Sum II
# ttungl@gmail.com
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # sol 1:
        # DFS
        # runtime: 79ms
        def dfs(root, cnt, path):
            if not root.left and not root.right and cnt == sum:
                res.append(path)
            if root.left:
                dfs(root.left, cnt + root.left.val, path + [root.left.val])
            if root.right:
                dfs(root.right, cnt + root.right.val, path + [root.right.val])
        #
        if not root:
            return []
        cnt, res = 0, []
        dfs(root, root.val, [root.val])
        return res
    
        # sol 2:
        # BFS
        # runtime: 72ms
        if not root:
            return []
        queue = [(root, root.val, [root.val])] 
        cnt, res = 0, []
        while queue:
            node, cnt, path = queue.pop(0)
            if not node.left and not node.right and cnt == sum:
                res.append(path)
            if node.left:
                queue.append((node.left, cnt + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, cnt + node.right.val, path + [node.right.val]))
        return res
                
        
        
    
        
    
