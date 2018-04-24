# 3. Longest Substring Without Repeating Characters
# ttungl@gmail.com

# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sol 1:
        # use dictionary and two pointers.
        # runtime: 79ms
        dic = {}
        res = last_match = 0
        for i, c in enumerate(s):
            if c in d and last_match <= dic[c]:
                last_match = dic[c] + 1
            else:
                res = max(res, i - last_match + 1)
            dic[c] = i
        return res
        
        
        # sol 2:
        # runtime: 95ms
        dic = {}
        res, last_match = 0, -1
        for i, c in enumerate(s):
            if c in dic and last_match < dic[c]:
                last_match = dic[c]
            res = max(res, i - last_match)
            dic[c] = i
        return res
        
                

