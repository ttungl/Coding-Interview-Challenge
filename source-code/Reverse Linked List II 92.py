# 92. Reverse Linked List II


 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # sol
        # three parts: 
        # 1. go to the index m.
        # 2. reverse within the range [m,n]
        # 3. connect m to n+1, and connect n to m-1.
        # 4. return dummy.next
        # runtime: 32ms
        if not head or m==n: return head

        dummyNode = prev = ListNode(0)
        dummyNode.next = head
        
        # 1. go to the index m.
        for _ in range(m-1): 
            prev = prev.next
        
        # 2. reverse within the range [m,n]
        node = None # reverse
        cur = prev.next
        for _ in range(n-m+1):
            next = cur.next
            cur.next = node
            node = cur
            cur = next
        
        # 3. connect m with n+1, connect n with m-1
        prev.next.next = cur
        prev.next = node
        
        # 4.
        return dummyNode.next
        
        

            


