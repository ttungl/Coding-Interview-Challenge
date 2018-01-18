# 271. Encode and Decode Strings

class Codec:
	# runtime: 172ms
    def encode(self, strs):
        out = []
        for s in strs:
            out.append('%s:' % len(s) + s)
        return ''.join(out)
    
    def decode(self, s):
        strs, i = [], 0
        while i<len(s):
            j = s.find(':', i) # Return the lowest index in the string where substring sub is found within the slice s[start:end]
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))