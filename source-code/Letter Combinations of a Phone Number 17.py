# Letter Combinations of a Phone Number

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # sol 1
        d = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6': 'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits)==0: return []
        return [a+b for a in self.letterCombinations(digits[:-1])
                    for b in self.letterCombinations(digits[-1])] or list(d[digits])
        
        # sol 2
        # recursion 
        d = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6': 'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        return [a+b for a in d.get(digits[:1], [])
                    for b in self.letterCombinations(digits[1:]) or ['']] or []
        
        # sol 3
        # backtracking DFS
        d = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6': 'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        if len(digits)==0: 
        	return res
        
        def DFS(digits, d, idx, path, res):
            if len(path)==len(digits):
                res.append(path)
                return
            [ DFS(digits, d, i+1, path+j, res) for i in xrange(idx, len(digits)) 
                                                  for j in d[digits[i]] ]
            
        DFS(digits, d, 0, "", res)
        return res
            