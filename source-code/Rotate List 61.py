# 61. Rotate List
# ttungl@gmail.com
# Given 1->2->3->4->5->NULL and k = 2,

# return 4->5->1->2->3->NULL.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # sol 1
        # make a circle, then rotate KK positions using KK = len - k % len
        if not head: 
            return
        ln = 0 # length of list
        p = head # pointer
        while p.next: # count the length of list
            p = p.next
            ln+=1
        p.next = head # circle the list
        ln+=1 # length of binding the tail to head. ln=5
        # p=1-2-3-4-5-null becomes p=..->5-1-2-3-4->..
        # ln = 5;
        # p=..->5-1-2-3-4->..
        x = ln - k % ln # if k=2: x=5-2%5=3; 
        while x > 0:  # x=3
            p = p.next # 
            x-=1 #
        # p= ..->3-4-5-1-2->..
        # head= 1-2-3-4-5    
        head = p.next # head = 4 because p=3 so p.next=4
        p.next = None # clear p.next
        return head # head = 4-5-1-2-3
                



        

