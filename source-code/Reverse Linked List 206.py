# 206. Reverse Linked List
# ttungl@gmail.com
# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iterative
        # runtime: 42ms
        next = None # or prev
        while head:
            head.next, head, next = next, head.next, head
        return next
        
        # recursive
        # runtime: 59 ms
        def revlist(head, prev=None):
            if not head: 
                return prev
            next = head.next
            head.next = prev
            return revlist(next, head)
        return revlist(head)

        # inplace
        # runtime: 39 ms
        node = None
        while head:
            next = head.next
            head.next = node
            node = head
            head = next
        return node
        
        
    
    
        
        
        
        