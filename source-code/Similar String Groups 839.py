# 839. Similar String Groups


# Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

# We are given a list A of unique strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

# Example 1:

# Input: ["tars","rats","arts","star"]
# Output: 2
# Note:

# A.length <= 2000
# A[i].length <= 1000
# A.length * A[i].length <= 20000
# All words in A consist of lowercase letters only.
# All words in A have the same length and are anagrams of each other.
# The judging time limit has been increased for this question.


class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # sol 1:
        # time O(MN^2)
        # runtime: 6132ms
        parents = {x : x for x in A}
        n, m = len(A), len(A[0])
        self.count = n
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parents[x] = y
                self.count -= 1
            #     return True
            # return False
        
        def similar(x, y):
            return sum(s!=t for s, t in zip(x, y)) == 2
        
        if len(A) <= 2*(10**4) ** 0.5: # tricky part
            for s, t in itertools.permutations(A, 2):
                if similar(s, t): 
                    union(s, t)
        else:
            for s in A:
                for i, j in itertools.combinations(range(m), 2):
                    t = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                    if t in parents: 
                        union(s, t)
                        
        return self.count
            
            



