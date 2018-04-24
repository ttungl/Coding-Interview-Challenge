# 424. Longest Repeating Character Replacement
# ttungl@gmail.com

# Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

# Note:
# Both the string's length and k will not exceed 104.

# Example 1:

# Input:
# s = "ABAB", k = 2

# Output:
# 4

# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input:
# s = "AABABBA", k = 1

# Output:
# 4

# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # similar to the longest substring k distinct.
        # len(str) - maxCharOccurrences <= k
        
        # sol 1:
        # use sliding window from i to j.
        # time O(n^2) space O(n)
        # runtime: 117ms
        count = collections.defaultdict(int)
        maxn = i = j = 0
        for i in range(1, len(s)+1):
            count[s[i-1]] += 1
            maxn = max(maxn, count[s[i-1]])
            if i - j - maxn > k:
                count[s[j]] -= 1
                j += 1
        return i-j
    
        # sol 2:
        # sliding window
        # runtime: 714ms
        count = collections.Counter()
        maxn = i = j = 0
        for i in range(1, len(s) + 1):
            count[s[i-1]] += 1
            maxn = count.most_common(1)[0][1]
            if i - j - maxn > k:
                count[s[j]] -= 1
                j += 1
        return i-j
        
        















