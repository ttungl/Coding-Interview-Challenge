# 449. Serialize and Deserialize BST


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # runtime: 122ms
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serialize_it(node):
            if node:
                # bst: pre-order
                strs.append(str(node.val))
                serialize_it(node.left)
                serialize_it(node.right)
            else:
                strs.append('#')  
        strs = []
        serialize_it(root)
        return ' '.join(strs)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserialize_it():
            val = next(vals)
            if val == '#': return None
            node = TreeNode(int(val))
            node.left = deserialize_it()
            node.right = deserialize_it()
            return node
                
        
        vals = iter(data.split())
        return deserialize_it()
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))