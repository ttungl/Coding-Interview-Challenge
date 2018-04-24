# 143. Reorder List
# ttungl@gmail.com

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # find the middle of list
        # reverse the second half of list
        # insert one by one each element in 1st and 2nd halves.
        # runtime: 170ms
        if not head: 
            return head
        
        pi = pj = head
        
        while pj.next and pj.next.next: # j goes as twice as i.
            pi, pj = pi.next, pj.next.next
        
        cur = pi.next # start from 2nd half.
        node = pi.next = None
        while cur: # reverse 2nd half.
            next = cur.next
            cur.next = node
            node = cur
            cur = next
        
        cur1, cur2 = head, node
        while cur2: # insert 
            next1, next2 = cur1.next, cur2.next
            cur1.next, cur2.next = cur2, next1
            cur1, cur2 = next1, next2
            
            
        
        







