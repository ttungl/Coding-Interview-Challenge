# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # sol1: Recursive
        # time: O(n); space: O(1)
        # runtime: 29ms
        if head and head.next:
            tmp = head.next 
            head.next = self.swapPairs(tmp.next) 
            tmp.next = head
            return tmp
        return head
            
        # sol2: Iterative
        # time: O(n); space O(1)
        # runtime: 45ms
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next 
            tmp.next  = head
            #
            pre.next  = tmp 
            head = head.next     
            pre  = tmp.next
        return dummy.next
    
        # sol 3: Iterative
        # To change from: pre -> a -> b -> b.next to pre -> b -> a -> b.next
        # runtime: 32ms
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next # current node
            b = a.next   # next node
            pre.next, b.next, a.next = b, a, b.next 
            pre = a
        return self.next
        
        
        
        
    