# replace words

# https://leetcode.com/problems/replace-words/description/

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # sol 1:
        # use string.startswith(word in dict) to check prefix and join them.
        # time: O(n^2)
        # space: O(n)
        # runtime: 315ms
        words = sentence.split(" ")
        for index in range(len(words)):
            for wordindict in dict:
                if words[index].startswith(wordindict):
                    words[index] = wordindict # replace by the root.
        return " ".join(words)
        
        ###############################
        # sol 2:
        # use trie (prefix) data structure (dictionary)
        # time O(n)
        # space O(n)
        # runtime: 92 ms
        trie = {}
		        
        for word in dict:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['.'] = '.'
            
        def process(s):
            t = trie
            for i, c in enumerate(s):
                if c not in t:
                    break
                t = t[c]
                if '.' in t:
                    return s[:i+1]
            return s
        
        return ' '.join(map(process, sentence.split()))

        # sol 3:
        # runtime: 260ms
        class TrieNode(object):
            def __init__(self):
                self.children = collections.defaultdict(list)

        class Solution(object):
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                node = self.root
                for c in word:
                    if c not in node.children:
                        node.children[c] = TrieNode()
                    node = node.children[c]
                node.children['.'] = '.'

            def searchPrefix(self, prefix):
                node = self.root
                for i, c in enumerate(prefix):
                    if '.' in node.children:
                        return prefix[:i]
                    if c not in node.children:
                        break
                    node = node.children[c]
                return prefix
                    
            def replaceWords(self, dict, sentence):
                """
                :type dict: List[str]
                :type sentence: str
                :rtype: str
                """
                for word in dict:
                    self.insert(word)
                new_words = []
                for word in sentence.split():
                    new_words.append(self.searchPrefix(word))
                return ' '.join(new_words)
                
                
                
                    
                
                
                
               
                    
                
                    
                
                
                


