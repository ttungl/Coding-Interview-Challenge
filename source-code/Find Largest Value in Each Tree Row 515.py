# 515. Find Largest Value in Each Tree Row
# ttungl@gmail.com

# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 

#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 

# Output: [1, 3, 9]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # sol 1:
        # level-order traversal, get max of each level.
        # runtime: 72ms
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            res.append(max(node.val for node in queue))
            queue = [leaf for q in queue for leaf in (q.left, q.right) if leaf]
        return res

        # sol 2:
        # level order traversal, get max of each level.
        # runtime: 78ms
        if not root: 
            return []
        res, queue = [], [root]
        while queue:
            res.append([node.val if node else None for node in queue])
            queue = [leaf for q in queue for leaf in (q.left, q.right) if leaf]
        return [max(i) for i in res]
    
    
        # sol 3:
        # BFS iterative
        # runtime: 100ms
        if not root:
            return []
        res, queue = collections.defaultdict(list), [(root, 0)]
        while queue:
            node, level = queue.pop()
            res[level].append(node.val)
            if node.right: 
                queue.append((node.right, level + 1))
            if node.left: 
                queue.append((node.left, level + 1))
        return [max(i) for i in res.values()]
                
                
        
        
        
