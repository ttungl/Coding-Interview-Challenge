# 764. Largest Plus Sign



class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        # sol 1:
        # time O(n^2) space O(n^2)
        # runtime: 1234ms
        if len(mines)==N**2: return 0 # corner case [[0,0]]
        grid = [['1' for _ in range(N)] for _ in range(N)]
        for i,j in mines: grid[i][j] = '0'
        grid_row = [''.join(row) for row in grid]
        grid_col = [''.join(col) for col in map(list, zip(*grid))]
        res = 1
        for i in range(N):
            for j in range(N):
                if grid[i][j]=='1':
                    while True:
                        if (j-res>=0 and j+res<N and i-res>=0 and i+res<N and
                           grid_row[i][j-res:j+res+1].count('0')==0 and
                           grid_col[j][i-res:i+res+1].count('0')==0):
                            res+=1                                     
                        else:  
                            break
        return res


