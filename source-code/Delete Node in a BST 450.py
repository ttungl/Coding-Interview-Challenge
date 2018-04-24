# Delete Node in a BST 450
# ttungl@gmail.com
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
       
        # base
        if not root: return None
        
        # traverse to the target.
        if key < root.val:   root.left  = self.deleteNode(root.left, key)
        elif key > root.val: root.right = self.deleteNode(root.right, key)

        else: # key = value
            # node has one left/right, return right/left.
            if not root.left: return root.right
            elif not root.right: return root.left
            
            ### replace right node to target node
            ### find min node on right. 
            # min_val = root.right
            # while min_val.left: min_val = min_val.left
            # min_val.left = root.left
            # return root.right
        
            # replace left node to target node
            # find min node on left.
            min_val = root.left
            while min_val.right: min_val = min_val.right
            min_val.right = root.right
            return root.left
        
        return root