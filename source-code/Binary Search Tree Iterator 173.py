# 173. Binary Search Tree Iterator
# ttungl@gmail.com

# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.



# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    # sol 1:
    # runtime: 102ms
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left    
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val
    
    # sol 2:
    # runtime: 97ms
    def __init__(self, root):
        self.queue = collections.deque()
        self.stack = collections.deque()
        while root or self.stack:
            if root:
                self.stack.append(root)
                root = root.left
            else:
                root = self.stack.pop()
                self.queue.append(root.val)
                root = root.right
                
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue
            
    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft()
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())