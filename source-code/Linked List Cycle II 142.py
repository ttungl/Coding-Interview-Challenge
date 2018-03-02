# 142. Linked List Cycle II

# Given a linked list, return the node where the cycle begins. 
# If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # sol 1:
        # runtime: 83ms
        if not head: 
            return None
        pi = pj = head
        while pj and pj.next:
            pi, pj = pi.next, pj.next.next
            if pi == pj:
                break
        else:
            return None
        
        while head != pi: # find a begin node.
            pi, head = pi.next, head.next
        return head
        
