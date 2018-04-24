# 32. Longest Valid Parentheses
# ttungl@gmail.com

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sol 1:
        # using stack
        # runtime: 65ms
        res, lst, stack = 0, -1, []
        for i in range(len(s)):
            if s[i] == '(': 
                if lst >= 0: # last time matching ")".
                    stack.append(lst)
                    lst = -1
                else: # at first or last index, not matching ")"
                    stack.append(i)
            else: # ")"
                if stack:
                    stk = stack.pop() 
                    if i - stk + 1 > res:
                        res = i - stk + 1
                    lst = stk
                else:
                    lst = -1 # unmatched ")".
        return res
            
        # sol 2
        # DP-1
        # runtime: 66ms
        dp = [0] * len(s)
        res = lcount = 0
        for i in range(len(s)):
            if s[i] == '(':
                lcount += 1  # left count
            elif lcount > 0:
                dp[i] = dp[i - 1] + 2 # pair
                dp[i] += (dp[i - dp[i]] if i >= dp[i] else 0)
                res = max(res, dp[i])
                lcount -= 1
        return res
        
        
        
