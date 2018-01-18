# 234. Palindrome Linked List

 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # sol 1
        # runtime: 105 ms
        # 1. reverse first half
        # 2. compare reversed first half and second half.
        rev = None # reverse
        p1 = p2 = head
        # 1: reverse 1st half
        while p1 and p1.next:
            p1 = p1.next.next
            rev, rev.next, p2 = p2, rev, p2.next # first evaluates the right side.
        if p1: 
            p2 = p2.next
        # 2: compare 1st and 2nd halves.
        while rev and rev.val==p2.val:
            p2 = p2.next
            rev = rev.next
        return not rev
            
        # sol 2
        # runtime: 135ms
        # time O(n); space O(1)
        # 1.find the middle node
        # 2.reverse the 2nd half
        # 3.compare the 1st and 2nd halves
        p1, p2, node = head, head, None
        # 1: find the mid node
        # when p1 reaches the end, 
        # p2 reaches the mid node.
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
        # 2: reverse the 2nd half.
        while p2:
            nxt = p2.next
            p2.next = node
            node = p2
            p2 = nxt
        # 3: compare two halves.
        while node:
            if node.val!= head.val: return False
            node, head = node.next, head.next
        return True
        
            
