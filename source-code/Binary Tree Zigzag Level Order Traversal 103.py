# 103. Binary Tree Zigzag Level Order Traversal

# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # sol 1:
        # use queue at each level, 
        # reverse queue order on each even level, 
        # keep queue order on each odd level
        # runtime: 42ms
        if not root:
            return []
        queue = [root]
        res, cnt = [], 0
        while queue:
            cnt += 1
            if cnt%2==0:
                res.append([i.val if i else None for i in queue[::-1]])
            else:
                res.append([i.val if i else None for i in queue])
            queue = [i for q in queue for i in (q.left, q.right) if i]
        return res
    
        # sol 2:
        # use depth on levels.
        # runtime: 41ms
        if not root:
            return []
        res = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            node, depth = queue.pop()
            if depth % 2 == 0:
                res[depth].append(0, node.val)
            else:
                res[depth].append(node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return res.values()
                
        
        

