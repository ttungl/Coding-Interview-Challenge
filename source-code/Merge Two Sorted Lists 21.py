# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # sol 2: mergesort
        # runtime: 46 ms
        # --
        dummy = node = ListNode(0) # init
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        # rest
        node.next = l1 if not l2 else l2
        return dummy.next

        # sol 1: built-in 
        # time O(n); space O(n)
        # runtime: 55ms
        # --
        res = []
        while l1:
            res.append(l1.val)
            l1 = l1.next
        while l2:
            res.append(l2.val)
            l2 = l2.next
        return sorted(res)
    
        # sol 3: priority queue
        # runtime: 95ms
        # --
        res, heap = [], []
        while l1:
            heapq.heappush(heap, l1.val)
            l1 = l1.next
        while l2:
            heapq.heappush(heap, l2.val)
            l2 = l2.next
        while heap:
            res.append(heapq.heappop(heap))
        return res
            
        
                
            
        
        

