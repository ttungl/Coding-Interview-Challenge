# 825. Friends Of Appropriate Ages
# ttungl@gmail.com
# Some people will make friend requests. The list of their ages is given 
# and ages[i] is the age of the ith person. 

# Person A will NOT friend request person B (B != A) if any of the following 
# conditions are true:

# age[B] <= 0.5 * age[A] + 7
# age[B] > age[A]
# age[B] > 100 && age[A] < 100
# Otherwise, A will friend request B.

# Note that if A requests B, B does not necessarily request A.  
# Also, people will not friend request themselves.

# How many total friend requests are made?

# Example 1:

# Input: [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
# Example 2:

# Input: [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
# Example 3:

# Input: [20,30,100,110,120]
# Output: 
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

# Notes:

# 1 <= ages.length <= 20000.
# 1 <= ages[i] <= 120.

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # sol 1:
        # runtime: 248ms
        def friendRequest(a, b):
            return not ((b <= a*0.5 + 7) or (b > a) or (b > 100 and a < 100))
        res = 0
        d = collections.Counter(ages)
        for a in d:
            for b in d:
                if friendRequest(a, b):
                    res +=  d[a] * (d[b] - (a == b))
        return res
        # return sum(friendRequest(a, b) * d[a] * (d[b] - (a == b)) for a in d for b in d)
        
        # sol 2:
        # use bisect
        # runtime: 381ms
        from bisect import bisect_right
        res, ages = 0, sorted(ages)
        for i in range(len(ages))[::-1]:
            a = ages[i]
            l = bisect_right(ages, a*0.5 + 7) 
            r = bisect_right(ages, a) - 1
            if (r - l) >=0: res += (r - l)
        return res
        
        
        
     










