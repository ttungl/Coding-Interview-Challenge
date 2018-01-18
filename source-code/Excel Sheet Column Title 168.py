# 168. Excel Sheet Column Title 

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # ABC -> A*26^2 + B*26^1 + C*26^0
        # use (n-1)%26 to get column title from number, append and divide 26 until n=0. Then reversed(res) to get result.
        # runtime: 26ms
        res = []
        while n > 0:
            res.append(string.ascii_uppercase[(n-1)%26]) # or append(chr((n-1)%26 + ord('A'))
            n=(n-1)/26
        return ''.join(reversed(res))
