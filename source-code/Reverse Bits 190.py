# 190. Reverse Bits
# ttungl@gmail.com
# Reverse bits of a given 32 bits unsigned integer.

# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
# return 964176192 (represented in binary as 00111001011110000010100101000000).

# Follow up:
# If this function is called many times, how would you optimize it?

# Related problem: Reverse Integer

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # sol 1
        # runtime: 39ms
        res = 0
        for i in range(32):
            res <<= 1
            res |= n & 1
            n >>= 1
        return res
    
        # sol 2:
        # runtime:
        res = str(bin(n)) # res = 0bxxxx
        pad = int(32 - len(res) + 2) * "0"
        return int(res[0:2] + res[2:][::-1] + pad, 2)
        
        









