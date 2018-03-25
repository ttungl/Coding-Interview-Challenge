# Google [P] Anagrams checking

class Solution(object):
	# find combinations of substring check them in str1 (GLE => GLE, GEL, LEG, LGE, EGL, ELG)
	def permute(self, nums):
	    return nums and [p[:i] + [nums[0]] + p[i:] for p in permute(nums[1:]) for i in range(len(nums))] or [[]]

	def anagram_check(self, str1, str2):
		
	    if len(str1) < len(str2):
	        str1, str2 = str2, str1

	    #if str2 is in str1 it is anagram return true 'GLE' =>Google
	    if str2 in str1:
	        return True
	    
	    # get all the permutations and check it in given string
	    p_codes = permute(str2)
	    
	    for i  in range(len(p_codes)):
	        if ''.join(p_codes[i]) in str1:
	            return True
	    return False

