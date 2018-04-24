# Generate Parentheses 22
# ttungl@gmail.com
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # use DFS/backtracking
        # runtime: 52ms
        def DFS(lst, start, end, max_val, strs):
            if len(strs) == max_val*2: 
                lst.append(strs)
                return
            if start < max_val: DFS(lst, start+1, end, max_val, strs+"(")
            if end < start: DFS(lst, start, end+1, max_val, strs+")")
            
        lst = []
        DFS(lst, 0, 0, n, "")
        return lst
    
