# Factor Combinations 254
# ttungl@gmail.com
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        ##########################
        # recursive 
        # runtime: 36ms
        def DFS(n, i, path, res): 
            while i*i <= n:                      # 2*2 <= 12; 2*2<=6; 3*3<=12; 
                if n % i==0:                     # 12%2==0; 6%2==0; 12%3==0
                    res += [path + [i, n/i]]     # res = [[] + [2, 6]]; [[2]+[2,3]]; [[]+[3,4]];
                    DFS(n/i, i, path + [i], res) # DFS(6, 2, [2], res); (3, 2, [2,2], res); 
                i+=1                             # i=3;
            return res
        res, path = [], []
        return DFS(n, 2, path, res)
    
    
        ##########################
        # recursive 
        # runtime: 45ms
        return [ft for i in range(2, int(n**0.5)+1) 
                      if n%i==0 
                   for ft in [[i, n/i]] + [[i] + ft 
                      for ft in self.getFactors(n/i) 
                         if ft[0] >= i]]
        
        ##########################
        # iterative
        # runtime: 42ms
        # time: O(n)
        # space: O(n)
        
        res, stack, i = [], [], 2
        while True:
            if i*i > n:                 # 2*2 > 12,6; 2*2 > 3; 3*3 > 6; 3*3 > 12; 3*3 > 4; 4*4>12
                if not stack:           # stack is not None; empty 
                    return res          # return res = [[2,2]+[3]]; [[2]+[6]]; [[3]+[4]]
                res.append(stack + [n]) # res = [[2,2]+[3]]; [[2]+[6]]; [[3]+[4]]
                i = stack.pop()         # i = 2 = stack.pop(); i = 2; i=3
                n *= i                  # n = 6 = 3*2; 12=6*2; 12=4*3 
                i += 1                  # i = 3 = 2+1; i=3; i=4;
            elif n % i == 0:            # 12 % 3==0; 6 % 2==0;  
                stack.append(i)         # stack = [3], 
                n/=i                    # n=4=12/3; 
            else:
                i+=1 
                
        
                    
        
            
        