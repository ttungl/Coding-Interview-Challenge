# 799. Champagne Tower

# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup (250ml) of champagne.

# Then, some champagne is poured in the first glass at the top.  When the top most glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has it's excess champagne fall on the floor.)

# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

# Now after pouring some non-negative integer cups of champagne, return how full the j-th glass in the i-th row is (both i and j are 0 indexed.)

# Example 1:
# Input: poured = 1, query_glass = 1, query_row = 1
# Output: 0.0
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

# Example 2:
# Input: poured = 2, query_glass = 1, query_row = 1
# Output: 0.5
# Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
 

# Note:

# poured will be in the range of [0, 10 ^ 9].
# query_glass and query_row will be in the range of [0, 99].


class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        # sol 1
        # DP solution (backtracking)
        # runtime: 162ms
        res = [[0.0 for _ in range(i)] for i in range(1, query_row + 2)] # make a tower
        res[0][0] = poured # init
        x, y = query_row, query_glass
        for i in range(query_row):
            for j in range(len(res[i])):
                percent = (res[i][j] - 1) / 2.0 # percent pouring 
                if percent > 0:
                    res[i+1][j] += percent 
                    res[i+1][j+1] += percent
        return res[x][y] if res[x][y] <= 1 else 1
    
        # sol 2:
        # backtracking
        # runtime: 275ms
        res = [poured] + [0.0] * 99
        for i in range(1, query_row + 1):
            for j in range(i, -1, -1):
                res[j] = max(res[j]-1, 0)/2.0 + max(res[j-1]-1,0)/2.0
        return min(res[query_glass], 1)







