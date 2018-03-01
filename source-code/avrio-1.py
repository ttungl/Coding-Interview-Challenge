
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# input1: S = byebye
#          b y e b y e
# S index: 0 1 2 3 4 5
# 		   b y e b y e b y e b y  e
#          0 1 2 3 4 5 6 7 8 9 10 11

# output1: 2


# input2: S = hihihi
# output2: 3

def solution(S):
    # write your code in Python 3.6
    def searchCyc(S, p): # p= [-1,0,0,0,1,2,3]
        tmp = S+S # tmp = byebyebyebye
        res, i, j = -1, 0, 0
        while i < len(tmp): # len(tmp) = 12
            while j>=0 and S[j]!=tmp[i]: # [j=0, S[0]==tmp[0]]; [j=1,S[1]==tmp[1]; [j=5,S[5]==tmp[5]]; [j=3,S[3]==tmp[6]]; [S[4]==tmp[7]]; [S[5]==tmp[8]]; [S[3]==T[9]];...]
                j = p[j] 
            i += 1 # i=1;2;6;7;8;9;10;11;12.
            j += 1 # j=1;2;6;4;5;6;4;5;6.
            if j == len(S): # [1!=6 ;2!=6; 6==6;4!=6;5!=6; 6==6;...;6==6]
                res += 1 # res=0; 1; 2.
                j = p[j] # j=p[6]=3; j=3; 3
        return res # 2
    
    p = [0]*(len(S)+1) # DP-1 
    i, j, p[0] = 0, -1, -1 # [-1, 0, 0, 0, 0, 0, 0]
    while i < len(S): # 
        while j>=0 and S[j] != S[i]: # [j=0, S[0]!=S[1]]; [j=0, S[0]!=S[2]]; [j=0, S[0]==S[3]]; [j=1, S[1]==S[4]]; [j=2, S[2]==S[5]];
            j = p[j] # j=-1;-1;
        i += 1 # i=1;2;3;4;5;6;
        j += 1 # j=0;0;0;1;2;3;
        p[i] = j # p[1]=0;p[2]=0;p[3]=0;p[4]=1;p[5]=2;p[6]=3;
    
    return searchCyc(S, p)
    
    
    pass