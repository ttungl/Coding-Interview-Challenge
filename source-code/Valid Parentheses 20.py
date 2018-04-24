# 20. Valid Parentheses
# ttungl@gmail.com
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # use stack
        # runtime: 32ms
        stack = []
        for i in s:
            if i == '{': stack.append('}') 
            elif i=='(': stack.append(')')
            elif i=='[': stack.append(']')
            elif not stack or i != stack.pop(): 
                return False
        return not stack