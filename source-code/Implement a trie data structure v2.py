# Implement a trie data structure v2
# src: https://youtu.be/BXeIu54mUg0


# Four methods in this implementation
# 1. insert_key(key, val, trie)
	# insert key into trie and put val into key's bucket

# 2. has_key(key, trie)
	# true if trie has key, otherwise, false.

# 3. retrieve_val(key, trie)
	# retrieves val from key's bucket

# 4. start_with_prefix(prefix, trie)
	# return list of all keys that begin with 
	# the prefix where prefix is a string of at least one character


class TrieNode(object):
    def __init__(self, k):
    	"""Initialize your data structure here."""
        self.children = {}
        self.val = 0

class Trie(object):        
    def __init__(self):
    	"""Initialize your data structure here."""
        self.root = TrieNode(None)

   	def insert_key(self, key):


   	def has_key():


   	def retrieve_val():


   	def start_with_prefix():


   	

