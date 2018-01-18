# 23. Merge k Sorted Lists

 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # sol 1: built-in solution
        # time: O(n^2); space O(n)
        # runtime: 92ms
        # --
        res = []
        for lst in lists:
            while lst:
                res.append(lst.val)
                lst = lst.next
        return sorted(res)
    
        # sol 2: mergesort
        # time O(n log n); space O(n)
        # runtime: 169ms
        # --
        if not lists: return None
        if len(lists)==1: return lists[0]
        def merge(list1, list2):
            dummy = node = ListNode(0)
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next
            # the rest   
            node.next = list1 if not list2 else list2
            return dummy.next
        mid = len(lists)/2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return merge(left, right)
        
        
        # sol 3: priority queue
        # time O(n log n); space O(n)
        # 1. push val to the heap
        # 2. pop val from the heap to the result
        # runtime: 282 ms
        # --
        res, heap = [], []
        # 1. push val to the heap
        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next
        # 2. pop val from the heap to the result
        while heap:
            res.append(heapq.heappop(heap))
        return res        
        



