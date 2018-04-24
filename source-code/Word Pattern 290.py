# Word Pattern 290
# ttungl@gmail.com

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # sol 1
        s = pattern
        t = str.split()
        return map(s.find, s)==map(t.index, t)
    
        
        # sol 2
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s)==len(t)
    
        
        # sol 3:
        # runtime: 29ms
        # pattern: "abba"
        # words: "dog cat cat dog"
        words = str.split()  # ['dog','cat','cat','dog']
        if len(pattern) != len(words): return False
        d, s = {}, set()                         
        for i in range(len(pattern)): # i=(0..3) in range(4)
            if pattern[i] not in d: # i=0: "a" not in {}; i=1: "b" not in {a:dog}; i=2: "b" in {a:dog; b:cat}, 
                if words[i] in s:   # i=0: dog not in (); i=1: cat not in (dog); 
                    return False
                else:                          
                    d[pattern[i]] = words[i]   # i=0: {a:dog}; i=1: {a:dog; b:cat}; 
                    s.add(words[i])            # i=0: (dog); i=1: (dog,cat)
            elif d[pattern[i]] != words[i]: 
                return False
        return True
        