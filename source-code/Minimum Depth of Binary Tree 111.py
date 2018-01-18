# 111. Minimum Depth of Binary Tree


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # sol 1: iterative
        # runtime: 59ms
        if not root:
            return 0
        queue = [(root, 1)] 
        while queue:
            node, level = queue.pop(0)
            if not node: return
            if not node.left and not node.right: return level
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))
        

        # sol 2: recursive
        # runtime: 69ms
        # --
        if not root: return 0
        if not root.left and not root.right: return 1
        minleft, minright = sys.maxsize, sys.maxsize
        
        if root.left:
            minleft = min(minleft, self.minDepth(root.left))
        if root.right:
            minright = min(minright, self.minDepth(root.right))
        
        return 1 + min(minleft, minright)