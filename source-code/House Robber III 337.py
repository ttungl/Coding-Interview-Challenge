# House Robber III 337

# The thief has found himself a new place for his thievery again. 
# There is only one entrance to this area, called the "root." 
# Besides the root, each house has one and only one parent house. 
# After a tour, the smart thief realized that 
# "all houses in this place forms a binary tree". 
# It will automatically contact the police if two directly-linked 
# houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight 
# without alerting the police.

#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # sol 1:
        # (first, second)
        # first: max#$ robbed if root not robbed (that's why leftrob[1] and rightrob[1], not x[0]).
        # second: max#$ robbed if root robbed.
        # time: O(n)
        # space: O(h)
        # runtime: 82ms
        def robsub(root):
            if not root: 
                return (0,0)
            leftrob, rightrob = robsub(root.left), robsub(root.right)
            first, second = root.val + leftrob[1] + rightrob[1], max(leftrob) + max(rightrob)
            return (first, second)
        return max(robsub(root))
        
        # sol 2
        # runtime: 66ms
        def DFS(node):
            if not node: 
                return (0,0) # stop
            leftrob, rightrob = DFS(node.left), DFS(node.right)
            # current level
            cur = [leftrob[0] + rightrob[0], leftrob[1] + rightrob[1]]
            return (cur[1] , max(cur[1], cur[0] + node.val))
        return DFS(root)[1]
            
        
        
        



















