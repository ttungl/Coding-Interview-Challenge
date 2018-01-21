# Word Pattern II 291

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # use dictionary d to store patterns, and backtrack if mismatch.
        # Note: "end of end"'s explanation: pattern=abcde | strs=redblue: try to match "a" to "red"~ 3 chars= 7-5+1.
        # and last +1 is for the range of python. So, len(strs)-len(pattern)+1+1.
        # runtime: 39ms
        def DFS(pattern, strs, d):
            if len(pattern)==0 and len(strs) > 0: return False
            if len(strs) == len(pattern) == 0: return True
            for end in range(1, len(strs)-len(pattern)+1+1): #+2: end of end.
                if pattern[0] not in d and strs[:end] not in d.values():
                    d[pattern[0]] = strs[:end]
                    if DFS(pattern[1:], strs[end:], d):
                        return True
                    del d[pattern[0]]
                elif pattern[0] in d and d[pattern[0]]==strs[:end]:
                    if DFS(pattern[1:], strs[end:], d):
                        return True
            return False
        
        return DFS(pattern, str, {})
    
            
        
        