# Kth Smallest Element in a BST 230.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # sol 1:
        # recursive
        # runtime: 76ms
        def DFS(node, count):
            if not node: return 
            DFS(node.left, count)
            count.append(node.val)
            DFS(node.right, count)
            return count
        return DFS(root, [])[k-1]
        
        
        # sol 2:
        # iterative
        # runtime: 76ms
        node, stack, state = root, [], False
        while not state:
            while node!=None:
                stack.append(node)
                node = node.left

            if stack != []:
                node = stack.pop()
                k -= 1
                if k == 0: 
                    return node.val
                node = node.right
            
            else:
                state = True
                
                
        # sol 3:
        # Use binary search
        # return k-th of k in BT.
        # runtime: 78ms
        def DFS(root): # get height of tree
            if not root: return 0
            return 1 + DFS(root.left) + DFS(root.right)
            
        c = DFS(root.left) # height on left. 
        if k <= c: # 5 <= c 
            return self.kthSmallest(root.left, k)
        elif k > c+1: # 5 > 4=c+1;
            return self.kthSmallest(root.right, k-1-c) # kth( , 1=5-1-3)
        return root.val
    
        
        
        
        
        