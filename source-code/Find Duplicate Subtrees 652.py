# 652. Find Duplicate Subtrees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # sol 1: use pre-order with hashmap (defaultdict(list)) to store the values of subtree.
        # Note: each preorder traversal returns the values of subtree. 
        # Then saves the subtree as a key in the hashmap nodes. 
        # and then returns the first node for every key in the nodes if there are at least 2 values.
        # time O(n) space O(log n)
        # runtime: 132ms
        # --
        def preorder_traversal(node): # Root, Left, Right
            if not node: return None
            vals = (str(node.val), 
                     preorder_traversal(node.left),
                     preorder_traversal(node.right))
            nodes[vals].append(node)
            return vals
        nodes = collections.defaultdict(list) # hashmap
        preorder_traversal(root)
        return [nodes[vals][0] for vals in nodes if len(nodes[vals]) > 1]
        
        
        # sol 2: use post-order with hashmap (defaultdict(list))
        # for each traversal, store values to hashmap. 
        # returns the second node for every key in the nodes if at least 2 values.
        # runtime: 302ms
        def postorder_traversal(node): # left,right,root
            if not node: return None
            vals = (postorder_traversal(node.left),
                    postorder_traversal(node.right),
                    str(node.val))
            nodes[vals].append(node)
            return vals
        nodes = collections.defaultdict(list) # hashmap
        postorder_traversal(root)
        return [nodes[vals][1] for vals in nodes if len(nodes[vals]) > 1]
            
          
        
        
        
        
        
        