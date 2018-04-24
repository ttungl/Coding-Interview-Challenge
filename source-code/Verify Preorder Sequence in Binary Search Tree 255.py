# 255. Verify Preorder Sequence in Binary Search Tree
# ttungl@gmail.com
# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

# You may assume each number in the sequence is unique.

# Follow up:
# Could you do it using only constant space complexity?


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # preorder: root, left, right
        # sol 1:
        # use stack 
        # time O(n) space O(n)
        # runtime: 91ms
        low = -1 << 31
        stack = []
        for i in preorder:
            if i < low:
                return False
            while stack and i > stack[-1]:
                low = stack.pop()
            stack.append(i)
        return True
        
        # sol 2:
        # time O(n) space O(1)
        # runtime: 169ms
        low = -1 << 31
        index = 0
        for i in preorder:
            if i < low:
                return False
            while index > 0 and i > preorder[index - 1]:
                low = preorder[index - 1]
                index -= 1
            preorder[index] = i
            index += 1
        return True
            
            

        