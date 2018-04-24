# Encode and Decode TinyURL 535
# ttungl@gmail.com
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/

class Codec:

    # sol 1:
    # runtime: 39ms
    def __init__(self): # constructor for class.
        self.d = {}
        
    def encode(self, longURL):
        key = hash(longURL) 
        self.d[key] = longURL
        return key
    
    def decode(self, shortURL):
        '''return original URL'''
        return self.d[shortURL]
    
    # ****************************
    # sol 2: 
    # runtime: 46ms
    def __init__(self):
        self.d = {}
        
    def encode(self, longURL):
        tinyurl = 'http://tinyurl.com/'
        
        def id_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase): # ref: https://stackoverflow.com/a/2257449/2881205
            return ''.join(random.choice(chars) for _ in range(size))

        while True:
            key = id_generator()
            if key not in self.d.values():
                self.d[key] = longURL
                return tinyurl+key
    
    def decode(self, shortURL):
        '''return original URL'''
        key = shortURL[19:]
        return self.d[key]
    
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
    
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

