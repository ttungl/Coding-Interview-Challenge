# 19. Remove Nth Node From End of List
# ttungl@gmail.com
# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # sol 1:
        # runtime: 44ms
        pi = pj = head
        for _ in range(n): # distance n btw i and j
            pj = pj.next

        if not pj: # check None
            return head.next

        while pj.next: # traverse to the end of list
            pi, pj = pi.next, pj.next
            
        pi.next = pi.next.next # remove n-th
        return head
    
        # sol 2:
        # use dummyNode
        # runtime: 46ms
        if not head: 
            return head
        # use dummy node
        dmNode = ListNode(0)
        dmNode.next = p = head
        for _ in range(n): # distance n
            p = p.next
        if not p: # check None
            return head.next
        while p.next: # traverse to the end of list
            head, p = head.next, p.next
        head.next = head.next.next # remove n-th
        return dmNode.next 
        
        
        
        

