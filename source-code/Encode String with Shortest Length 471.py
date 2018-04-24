# 471. Encode String with Shortest Length

# ttungl@gmail.com
# Given a non-empty string, encode the string such that its encoded length is the shortest.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

# Note:
# k will be a positive integer and encoded string will not be empty or have extra space.
# You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
# If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
# Example 1:

# Input: "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
# Example 2:

# Input: "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
# Example 3:

# Input: "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
# Example 4:

# Input: "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
# Example 5:

# Input: "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".


class Solution(object):
    
    def encode(self, s, memo = collections.defaultdict(str)):
        """
        :type s: str
        :rtype: str
        """
        # sol 1
        # use a dict to store res.
        # use s+s to find index of repeated substring.
        # two params: onepart and multiparts. 
        # runtime: 564ms
        if s not in memo:
            n = len(s)
            i = (s + s).find(s, 1) # find repeated substring pattern. s[:i+1].
            one = '%d[%s]' % (n / i, self.encode(s[:i])) if i < n else s # one part
            multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, n)] # multiparts(subprobs)
            memo[s] = min([s, one] + multi, key=len)
        return memo[s]
    
        

































