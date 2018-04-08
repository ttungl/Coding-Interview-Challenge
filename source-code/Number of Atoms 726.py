# 726. Number of Atoms

# Given a chemical formula (given as a string), return the count of each atom.

# An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

# 1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

# Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

# Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

# Example 1:
# Input: 
# formula = "H2O"
# Output: "H2O"
# Explanation: 
# The count of elements are {'H': 2, 'O': 1}.
# Example 2:
# Input: 
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: 
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# Example 3:
# Input: 
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation: 
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# Note:

# All atom names consist of lowercase letters, except for the first character which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.


class Solution(object):
	def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        # split into chars.
        # Three cases:
        # + Open parenthesis: push a new dict to stack to keep track of atoms and its count.
        # + Close parenthesis: check if next index is a number, then multiply number of all atoms on the top of stack.
        # + Atom: check if next index is a number, add that atom to top of stack and its count.
        # time O(n*n) space O(n)
        # runtime: 36ms
        import re
        tokens = list(filter(lambda c: c, re.split('([A-Z]{1}[a-z]?|\(|\)|\d+)', formula)))
        stack = [collections.defaultdict(int)]
        i = 0
        while i < len(tokens):
        	token = tokens[i]
        	if token == '(':
        		stack.append(collections.defaultdict(int))

        	else: # close round bracket or atom cases.
        		
        		count = 1
        		# check next index is a number 
        		if i + 1 < len(tokens) and tokens[i+1].isdigit():
        			count, i = int(tokens[i+1]), i+1

        		# 1.close round bracket case. 
        		atoms = stack.pop() if token == ')' else {token : 1}

        		# 2.if atom case: combine counter to all atoms on top of stack. 
        		for a in atoms:
        			stack[-1][a] += atoms[a] * count

        	i += 1

        return ''.join([atom + (str(count) if count>1 else '') for atom, count in sorted(stack[-1].items())])








