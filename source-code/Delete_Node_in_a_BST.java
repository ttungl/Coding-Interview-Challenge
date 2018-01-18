// 450. Delete_Node_in_a_BST


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        // search key in the tree, if key is found, return root.
        // if key found at node n:
        //    + node has no left/right: return null
        //    + node has either left/right: return right/left
        //    + node has both left and right: 
        //          + find minval of right.
        //          + set minval to current node found
        //          + delete min in right.
 		// time complexity: O(height of tree)
 		// space complexity: O(n)

        // search for x
        if (root==null) return null;
        
        if (root.val > key){ // left subtree
            root.left = deleteNode(root.left, key); 
        } else if (root.val < key) { // right subtree
            root.right = deleteNode(root.right, key);
            
        } else { // key is found
            
            if (root.left==null) return root.right;
            else if(root.right==null) return root.left;
            
            // node has both left and right
            TreeNode minValue = root.right;
            while (minValue.left !=null) minValue = minValue.left;
            
            minValue.left = root.left;
            return root.right;
        }
        return root;
        
        
        
    }
}