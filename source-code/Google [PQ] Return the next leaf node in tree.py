# Return the next leaf node in tree


# Given a tree, if query a leaf node, return the next leaf node. If the queried node is an internal node, return whatever you want. You can define the node structure. (Not a binary tree)

# Example:

#             a    
#         z        x      
#    w  z  y      o   b
# If I query 'z' return 'y'. If I query 'y', return 'o'. If I query 'b', return null.



class TreeXNode(object):
	def __init__(object, val=0):
		self.val = val
		self.children = {}


class Solution(object):

	def __init__(self, res=0):
		self.root = TreeXNode()
		self.found = False
		self.res = res

	def isLeaf(self, node):
		for i in node.children:
			if i:
				return False
		return True 


	def findLeaf(self, node, query):

		if not node or self.res != 0:
			return

		if isLeaf(node) and self.found:
			self.res = node.val # next leaf of query
			return

		if node.val == query:
			self.found = True
			if not isLeaf(node):
				self.res = -1 # internal node.


	def nextLeaf(self, query):
		
		node = self.root

		for i in node.children:
			findLeaf(i, query)


print(nextLeaf(query))






		# if not node:
		# 	return None
		
		# leafNodes = []
		# tem = node 
		# while node:
		# 	if not node.children:
		# 		leafNodes.append(node.val)
		# 	node = node.children

		# if query in leafNodes:
		# 	index = leafNodes[query]
		# 	if leafNodes[index + 1]:
		# 		return leafNodes[index + 1]
		# 	return None
		# node = tem.next 

