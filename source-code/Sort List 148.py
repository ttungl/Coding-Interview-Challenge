# 148. Sort List
# ttungl@gmail.com
# Sort a linked list in O(n log n) time using constant space complexity.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # sol 1:
        # use dummy node
        # time O(n log n) space O(n)
        # runtime: 366ms
        def merge(l1, l2):
            dummy = node = ListNode(None)
            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            node.next = l1 or l2
            return dummy.next
        #
        # check invalidation
        if not head or not head.next:
            return head
        # split the list into two parts
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        second = slow.next # second half.
        # cut the first half.
        slow.next = None  
        # recursive
        left = self.sortList(head)
        right = self.sortList(second)
        return merge(left, right)
            


        # sol 2:
        # without dummy node
        # runtime: 408ms
        def merge(l1, l2):
            if l1.val > l2.val:
                l1, l2 = l2, l1
            head = node = l1
            l1 = l1.next
            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            node.next = l1 or l2
            return head
        #
        if not head or not head.next:
            return head
        # split the list into two halves.
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        second = slow.next 
        slow.next = None # cut down the first half.
        # recursive
        left = self.sortList(head)
        right = self.sortList(second)
        return merge(left, right)


        # sol 3:
        # in-place
        # time O(n log n) space O(n)
        # runtime: 110ms
        if not head:
            return head
        res = []
        node = head
        while node: # O(n)
            res.append(node.val)
            node = node.next
        res.sort() # O(n log n)
        node = head
        for i in res:
            node.val = i
            node = node.next
        return head

        
























