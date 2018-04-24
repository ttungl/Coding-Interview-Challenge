# 374. Guess Number Higher or Lower

# ttungl@gmail.com
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # sol 1:
        # use BS
        # time O(log n) space O(1)
        # runtime: 51ms
        left, right = 1, n
        while left+1 < right: # two more candidates after loop.
            mid = left + (right-left)/2
            x = guess(mid)
            if x==0: return mid
            elif x==-1: right = mid
            elif x==1: left = mid

        if guess(left)==0: return left
        if guess(right)==0: return right
        return None
        
        # sol 2:
        # use BS
        # runtime: 36ms
        bs = [1, n]
        while True:
            num = (bs[0] + bs[1])/2
            x = guess(num)
            if x==0: return num
            elif x<0: bs[1] = num-1
            elif x>0: bs[0] = num+1
        
        
        