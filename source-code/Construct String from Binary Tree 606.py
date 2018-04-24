# 606. Construct String from Binary Tree
# ttungl@gmail.com
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /    
#   4     
# Output: "1(2(4))(3)"
# Explanation: Originallay it needs to be "1(2(4)())(3()())", 
# but you need to omit all the unnecessary empty parenthesis pairs. 
# And it will be "1(2(4))(3)".


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # sol 1: recursive
        # runtime: 69ms
        if not t: return ""
        res = []
        subleft = self.tree2str(t.left)
        subright = self.tree2str(t.right)
        if subleft or subright: res.append("(%s)" % subleft)
        if subright: res.append("(%s)" % subright)
        return str(t.val) + ''.join(res)
    
        # sol 2: recursive
        # runtime: 69ms
        if not t: return ""
        subleft = "(%s)" % (self.tree2str(t.left) if t.left or t.right else "")
        subright = "(%s)" % (self.tree2str(t.right) if t.right else "")
        return ("%s%s%s" % (str(t.val), subleft, subright)).replace("()","")
        
        