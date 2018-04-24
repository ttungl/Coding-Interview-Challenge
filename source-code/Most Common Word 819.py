# 819. Most Common Word
# ttungl@gmail.com
# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

# Example:
# Input: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.
 

# Note:

# 1 <= paragraph.length <= 1000.
# 1 <= banned.length <= 100.
# 1 <= banned[i].length <= 10.
# The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
# paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
# Different words in paragraph are always separated by a space.
# There are no hyphens or hyphenated words.
# Words only consist of letters, never apostrophes or other punctuation symbols.


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # sol 1:
        # "\b" word boundary such as "ad dc"; 
        # "\w" word character [A-Za-z0-9_].
        # "\s" whitespace.
        # "^" begins a string, "$" ends a string; 
        # "[]" contains matching character class.
        # runtime: 61ms
        import re
        words = re.sub(r'[^\w\s]', ' ', paragraph).lower().split()
        res = collections.Counter(words).most_common()
        return iter(w for w, cnt in res if w not in set(banned)).next()
        
    
        # sol 2:
        # runtime: 46ms
        # remove punctuations 
        import re
        paragraph = re.sub(r'[^\w\s]','',paragraph)
        d = collections.defaultdict(int)
        for word in paragraph.lower().split(): 
            if word not in set(banned): 
                d[word] += 1
        return max(d, key=d.get)
    
    
    
    
    
        
        
        
        
        
    
            
        


