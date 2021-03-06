# 15. 3Sum
# ttungl@gmail.com

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# --
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sol 1:
        # binary search
        # runtime: 1476ms
        res = []
        nums.sort() ## tricky

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i + 1, len(nums)-1

            while lo < hi:

                s = nums[i] + nums[lo] + nums[hi]
        
                if s < 0: lo += 1
        
                elif s > 0: hi -= 1
        
                else: # s = 0

                    res.append((nums[i],nums[lo],nums[hi]))
                    
                    while lo < hi and nums[lo] == nums[lo + 1]: lo += 1  

                    while lo < hi and nums[hi] == nums[hi - 1]: hi -= 1

                    lo += 1
                    hi -= 1
        return res
    



        # sol 2:
        # runtime: 1227ms
        if len(nums) < 3:
            return []
        nums.sort() # [-4, -1, -1, 0, 1, 2]
        res = set() # use set() takes less space than list.
        
        for i, v in enumerate(nums[:-2]): # n=[-4,-1,-1,0]
            if i >= 1 and v == nums[i-1]: # i=1, v=-1, n[1-1]=n[0]=-4 //;i=2, v=-1, n[2-1]=n[1]=-1
                continue

            d = {} 
            for x in nums[i+1:]: # x in n[1+1]=n[2:]=[-1,0]
                if x not in d: # 
                    d[-v-x] = 1 # d[-1-(-1)]=d[0]=1; 
                else:
                    res.add((v, -v-x, x)) # res=(-1, 0, -1)
        return map(list, res) # or use "list(s for s in res)"
    




        # sol 3:
        # runtime: 580ms
        counter = collections.defaultdict(int)

        for num in nums: counter[num] += 1
        
        if 0 in counter and counter[0] > 2: 
            res = [[0, 0, 0]]
        else: res = []
        
        uniques = counter.keys()  
        
        pos = sorted(p for p in uniques if p > 0)
        neg = sorted(n for n in uniques if n < 0)
        
        for p in pos:
            for n in neg:
                inverse = -(p + n)  
                if inverse in counter:
                    if inverse == p and counter[p] > 1:
                        res.append([n, p, p])
                    elif inverse == n and counter[n] > 1:
                        res.append([n, n, p])
                    elif n<inverse< p or inverse == 0:
                        res.append([n, inverse, p])
        return res
                    
                    
        
    