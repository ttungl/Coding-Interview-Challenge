# matterport
# 01/25/2018

# // I call this problem: "circularly sorted array"
# // We have an array sorted in an odd format:
# // [5 6 7 *1 2 3 4]
# // [5 6 *1 2 3]

# // Writ a function that returns true if a target number exists in a give array
# def circularArray(nums, target): # nums: array; target: int; return bool

# sol 1: naive
# time O(n) space O(1)
for i in nums:
   if i==target: 
       return True
return False

# sol 2:
# binary search
lo, hi = 0, len(nums)-1 #  [5 *6 1 2 3]: lo=0, hi=4; target=6

while lo < hi: # 0<4; 0<2;
   mid = lo + (hi-lo)/2 # m=2; m=0+(2/2)=1
   if nums[mid]==target: # 1: true; 6==6: true
       return True
   elif nums[mid] < target: hi = mid # 1 < 6; hi=2
   elif nums[mid] > target: lo = mid
return False

# sol 3:
while lo < hi:
   mid=lo + (hi-lo)/2
   if nums[mid]==target: return True
   if nums[mid] > target: 
       if nums[lo] <= target <= nums[mid]: hi = mid-1
       else: lo = mid+1
   else:
       if nums[mid] <= target <= nums[hi]: lo = mid +1
       else: hi = mid-1
return False
   
   
   
   