# 141. Linked List Cycle

# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # use two pointers, one is faster than another.
        # if faster pointer meets slower pointer, cycle detected.
        # runtime: 73ms
        if not head: 
            return False

        pi = pj = head
        
        while pj.next and pj.next.next:
            pi, pj = pi.next, pj.next.next
            if pi == pj: return True
        return False
        









