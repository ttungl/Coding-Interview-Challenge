# 138. Copy List with Random Pointer


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # sol 1:
        # using dictionary
        # runtime: 119ms
        dic = collections.defaultdict(lambda: RandomListNode(0))
        dic[None] = None
        node = head
        while node:
            dic[node].label = node.label
            dic[node].next = dic[node.next]
            dic[node].random = dic[node.random]
            node = node.next
        return dic[head]
        
        # sol 2:
        # runtime: 135ms
        dic = collections.defaultdict(lambda: RandomListNode(0))
        dic[None] = None
        node = head
        while node:
            dic[node].label = node.label
            if node.next==None: dic[node].next = None
            else: dic[node].next = dic[node.next]
            if node.random == None: dic[node].random = None
            else: dic[node].random = dic[node.random]
            node = node.next
        return dic[head]
    
        
        


