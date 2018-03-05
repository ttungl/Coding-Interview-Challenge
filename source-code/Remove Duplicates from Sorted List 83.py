# 83. Remove Duplicates from Sorted List

# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # sol 1:
        # runtime: 62ms
        if not head: 
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next # move to next element since duplicated.
            else:
                p = p.next 
        return head
            
        # sol 2:
        # runtime:
        
            










