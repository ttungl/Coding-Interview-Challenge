# 2. Add Two Numbers
# ttungl@gmail.com

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # sol 1:
        # reverse the lists
        # sum operation
        # add back to the list and return.
        # runtime: 227ms
        # --
        lst1, lst2 = [], []
        lst = 0
        def revlist(head, node=None):
            while head:
                next = head.next
                head.next = node
                node = head
                head = next
            return node
        l1 = revlist(l1) 
        l2 = revlist(l2)
        while l1:
            lst1.append(l1.val); l1 = l1.next
        while l2:
            lst2.append(l2.val); l2 = l2.next
        # convert list to number
        ls1 = int(''.join(map(str, lst1))) 
        ls2 = int(''.join(map(str, lst2))) 
        # sum ops
        lst = ls1 + ls2
        res, chk = [], lst
        while lst>0:
            x = lst%10
            res.append(x)
            lst /= 10
        return res if chk!=0 else [0] 
    
        
        # sol 2: better (beat 59%) **
        # runtime: 125ms
        # --
        cur = dummy = ListNode(0) # init linked lists
        carry = 0
        while l1 or l2 or carry:
            num = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = num/10
            cur.next = ListNode(num % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
    
    
        # sol 3: beats 36%
        # runtime: 140ms
        # --
        def toInt(node):
            return node.val + 10 * toInt(node.next) if node else 0
        def toList(i):
            node = ListNode(i % 10)
            if i > 9: # overflow
                node.next = toList(i / 10)
            return node
        return toList(toInt(l1) + toInt(l2))
        
    
        
        
        
        