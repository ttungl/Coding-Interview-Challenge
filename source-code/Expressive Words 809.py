# 809. Expressive Words

# ttungl@gmail.com
# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  Here, we have groups, of adjacent letters that are all the same character, and adjacent characters to the group are different.  A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the first example, and "i" would be extended in the second example.  As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that string.

# For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.  Formally, we are allowed to repeatedly choose a group (as defined above) of characters c, and add some number of the same character c to it so that the length of the group is 3 or more.  Note that we cannot extend a group of size one like "h" to a group of size two like "hh" - all extensions must leave the group extended - ie., at least 3 characters long.

# Given a list of query words, return the number of words that are stretchy. 

# Example:
# Input: 
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.
# Notes:

# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters




class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # sol 1:
        # breakString method splits string into groups of chars.
        # for each word, check if all chars in word exist in string, 
        # if so, then check the length of chars in both meets the requirements,
        # where the length of chars in string must be greater than or equal 
        # the length of chars in word.
        # time O(m*n) space O(n)
        # runtime: 95ms
        def breakString(s): 
            res = []
            i = j = 0
            while i < len(s):
                while i < len(s) and (s[j]==s[i]):
                    i+=1
                res.append(s[j:i])
                j = i
            return res
        #
        string = breakString(S)
        count = [len(i) for i in string]
        res = 0
        k = 3 # extended length 
        for w in words:
            word = breakString(w)
            wCount = [len(i) for i in word]
            uniqueCharStr = [i if len(i)==1 else i[0] for i in string]
            uniqueCharWord = [i if len(i)==1 else i[0] for i in word]
            if uniqueCharStr != uniqueCharWord: # check if all chars available on both.
                continue
            res += all(c1 >= max(c2, k) or c1==c2 for c1, c2 in zip(count, wCount))
        return res
        
        
        
        
        
        
        
        
        
        
        


