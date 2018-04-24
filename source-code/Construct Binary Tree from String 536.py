# 536. Construct Binary Tree from String

# ttungl@gmail.com

# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:
#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        # sol: recursive
        # runtime: 549ms
        # --
        idx = s.find('(')
        if idx < 0:
            return TreeNode(int(s)) if s else None
        balance = 0
        for jdx, u in enumerate(s):
            if u == '(': balance += 1
            if u == ')': balance -= 1
            if jdx > idx and balance == 0:
                break
                
        root = TreeNode(int(s[:idx]))
        root.left = self.str2tree(s[idx+1:jdx])
        root.right = self.str2tree(s[jdx+2:-1])
        return root
    
        # sol: stack
        # runtime: 142ms
        # --
        if not s: return None
        s = s.split('(')
        root = TreeNode(int(s[0]))
        stack = [root]
        for i in range(1, len(s)):
            v = s[i].rstrip(')')
            new = TreeNode(int(v))
            if stack[-1].left:
                stack[-1].right = new
            else:
                stack[-1].left = new
            nrange = len(s[i]) - len(v)
            if nrange == 0: stack.append(new)
            [stack.pop() for _ in range(nrange-1)]
        return root
        
        # sol: recursive
        # replace "(" to "t(" in '4(2(3)(1))(6(5))' to 't(4,t(2,t(3),t(1)),t(6,t(5)))'.
        # runtime: 198ms
        def t(val, left=None, right=None):
            # preorder traversal
            node, node.left, node.right = TreeNode(val), left, right
            return node
        return eval('t(' + s.replace('(', ',t(') + ')' ) if s else None
        
        


