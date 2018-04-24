# 677. Map Sum Pairs
# ttungl@gmail.com

# Implement a MapSum class with insert, and sum methods.

# For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

# For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

# Example 1:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5



# sol 1
# runtime: 38ms
class TrieNode(object):
    def __init__(self, v=0):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict()
        self.count = v
        
        
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keys = collections.defaultdict()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        diff = val - self.keys.get(key, 0)
        self.keys[key] = val
        
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count += diff

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count
                
                
# sol 2:
# runtime: 31ms
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.x[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        a = 0
        for i in self.x.keys():
            if i[:len(prefix)] == prefix:
                a+=self.x[i]
        return a



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

