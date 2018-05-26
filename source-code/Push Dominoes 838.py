# 838. Push Dominoes

# There are N dominoes in a line, and we place each domino vertically upright.

# In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

# After each second, each domino that is falling to the left pushes the adjacent domino on the left.

# Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

# Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

# Return a string representing the final state. 

# Example 1:

# Input: ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
# Example 2:

# Input: "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
# Note:

# 0 <= N <= 10^5
# String dominoes contains only 'L', 'R' and '.'

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        # sol 1:
        # use DP
        # time O(n) space O(n)
        # runtime: 553ms
        dp = [0]*len(dominoes) # distance from current index to L/R.
        lst = list(dominoes)
        n = len(lst)
        leftDist, rightDist = None, None

        for i, val in enumerate(dominoes): # right
            if val == 'R':
                rightDist = 0
            elif val == 'L':
                rightDist = None
            elif rightDist != None:
                rightDist += 1
                lst[i] = 'R'
                dp[i] = rightDist

        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                leftDist = 0
            elif dominoes[i] == 'R':
                leftDist = None
            elif leftDist != None:
                leftDist += 1
                if leftDist < dp[i] or lst[i]=='.': lst[i] = 'L' 
                elif leftDist == dp[i]: lst[i] = '.'
        return ''.join(lst)
        

        
