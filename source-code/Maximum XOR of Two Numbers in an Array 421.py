# 421. Maximum XOR of Two Numbers in an Array
# ttungl@gmail.com

# Given a non-empty array of numbers, a0, a1, a2, … , a(n-1), where 0 ≤ ai < 2^31.

# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

# Could you do this in O(n) runtime?

# Example:

# Input: [3, 10, 5, 25, 2, 8]

# Output: 28

# Explanation: The maximum result is 5 ^ 25 = 28.


class TrieNode(object):
	def __init__(self):
		self.children = collections.defaultdict(list)


class Solution(object):

	def __init__(self):
		self.root = TrieNode()


	def insert(self, num):
		node = self.root
		for i in range(32)[::-1]:
			cur = (num >> i) & 1 # means: (num divide by 2^i) and 1. 
			if cur not in node.children:
				node.children[cur] = TrieNode()
			node = node.children[cur]

	def findMaximumXOR(self, nums):
		# sol 1
        # Use Trie() keep groups 0 and 1.
        # From left bit to right, try to separate numbers into two groups with bits 1s and bits 0s.
        # if divisable into those groups, we want to XOR one number of group bits 0s 
        # and one number of group bits 1s.
        # Then, for next bit, we want to divide groups bits 0s from prev bit, so on so forth.
        # To maximum XOR, xor groups [zeros_pairs,ones_pairs] and [mix_01,mix_10].
        # runtime: 3573ms
		res = 0
        for num in nums:
            self.insert(num)

        for num in nums:
            cur, node = 0, self.root
            for i in range(32)[::-1]:
                idx = (num >> i) & 1 # (num divide by 2^i) and 1.
                if node.children[idx ^ 1]:
                    cur += 1 << i # (1 multiply by 2^i)
                    node = node.children[idx ^ 1]
                else:
                    node = node.children[idx]
            res = max(res, cur)
        return res

        # sol 2:
        # runtime: 139ms
        if len(nums)==2: 
            return nums[0]^nums[1]
        
		res = 0
        nums_set = set(nums)
        bin_len = len(bin(max(nums_set)))-2 # "-2 means minus '0b' in bin='0b0100'."
        max_xor = 2**bin_len-1
        
        while max_xor > 0:
            for num in nums_set:
                if max_xor ^ num in nums_set: 
                    return max_xor
            max_xor -= 1
        return max_xor






















