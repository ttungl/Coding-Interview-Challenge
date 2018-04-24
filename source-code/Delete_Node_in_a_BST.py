# 450. Delete_Node_in_a_BST
# ttungl@gmail.com
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
 		# // search key in the tree, if key is found, return root.
 		# // if key found at node n:
 		# //    + node has no left/right: return null
 		# //    + node has either left/right: return right/left
 		# //    + node has both left and right: 
 		# //          + find minval of right.
 		# //          + set minval to current node found
 		# //          + delete min in right.
 		# // time complexity: O(height of tree)
 		# // space complexity: O(n)
       
        if root is None: 
        	return None

        # search the key
        if root.val > key: 
            root.left = self.deleteNode(root.left, key)

        elif root.val < key: 
            root.right = self.deleteNode(root.right, key)

        else: # key is found
            
            if root.left is None: 
                return root.right
            elif root.right is None: 
                return root.left
            
            minValue = root.right
            while minValue.left: # find min value
                minValue = minValue.left
            # replace current found    
            minValue.left = root.left
            return root.right
        
        return root













