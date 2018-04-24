# 779. K-th Symbol in Grammar
# ttungl@gmail.com
# On the first row, we write a 0. Now in every subsequent row, 
# we look at the previous row and replace each occurrence of 0 with 01, 
# and each occurrence of 1 with 10.

# Given row N and index K, return the K-th indexed symbol in row N. 
# (The values of K are 1-indexed.) (1 indexed).

# Examples:
# Input: N = 1, K = 1
# Output: 0

# Input: N = 2, K = 1
# Output: 0

# Input: N = 2, K = 2
# Output: 1

# Input: N = 4, K = 5
# Output: 1

# Explanation:
# row 1: 0
# row 2: 01
# row 3: 0110
# row 4: 01101001

# Note:
# N will be an integer in the range [1, 30].
# K will be an integer in the range [1, 2^(N-1)].


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # sol 1: TLE
        if N==1 and K==1: return 0
        if N==1 and K>N: return -1
        tem = ""
        st="0"
        d = ("01", "10")
        # N=4,K=5; range(2,5) ~ 2,3,4.
        for i in range(2, N+1): # i=2; i=3; i=4; 
            for j in st: # st=0; st=01;
                tem += d[int(j)] # tem=d[0]=01; tem=0110
            st = tem # st=01;=0110;
            tem=""
        return int(list(st)[K-1])
        
        # sol 2:
        # runtime: 49ms
        # when N is increased by 1, the sequence extends by flipping itself, e.g. 0110 -> 0110 1001. 
        # Those extended Ks are exactly the originals with a prefixing 1 in their binary representations, 
        # which exactly changes the parity of the number of 1s. 
        # current row:  K   = 1   2    3    4    5    6    7    8    9     10
        # previous row: K-1 = 0   1    10   11  100   101  110  111 1000  1001     
        # output:   		  0   1    1     0   1     0    0   1    1     0
        return bin(K-1).count("1")%2
        
        # sol 3:
        # current row is double K of previous 
        # runtime: 31ms
        flip=0
        while K>1:  			# K=5;=3;=2
            flip += K%2 + 1     # flip=2;=4;=5;
            K=(K+1)/2           # K=3;=2;=1;
        return flip%2           # f%2=1
        































        
        
        


