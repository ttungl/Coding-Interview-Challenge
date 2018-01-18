# 104. Maximum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # sol 1: recursion (DFS)
        # time O(logn); space O(n)
        # runtime: 86ms
        # --
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
        # sol 2: iterative (BFS) using stack for level order
        # count the number of level in binary tree
        # runtime: 48ms
        # --
        if not root: return 0
        stack, level = [root], 0
        # count the level
        while stack:
            next = [] # next level
            while stack:
                top = stack.pop()
                if top.left: next.append(top.left)
                if top.right: next.append(top.right)
            stack = next
            level+=1
        return level
                
        
        # sol 3: iterative using queue for level order
        # runtime: 43ms
        # --
        if not root: return 0
        queue, level = collections.deque([root]), 0
        while queue:
            next = collections.deque() # next level
            while queue:
                head = queue.popleft() # return an element from left side of deque. (head/tail of queue)
                if head.left: next.append(head.left)
                if head.right: next.append(head.right)
            queue = next
            level+=1
        return level
                
                
            
        