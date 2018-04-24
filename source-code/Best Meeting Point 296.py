# 296. Best Meeting Point
# ttungl@gmail.com

# A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# For example, given three people living at (0,0), (0,4), and (2,2):

# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0

# The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.


class Solution(object):
    # sol 1:
    # find a set of groups (coordinates), sort ends,
    # use two pointers to update manhattan's distance
    # with two lists I and J.
    # time O(m*n) space O(n)
    # runtime: 46ms
    def totalMin(groups):
        ans, i, j = 0, 0, len(groups)-1
        I, J = sorted([k[0] for k in groups]), sorted([k[1] for k in groups])
        while i < j:
            ans += I[j] - I[i] # p2.x - p1.x
            ans += J[j] - J[i] # p2.y - p1.y
            i += 1
            j -= 1
        return ans
    groups = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]!=0]
    return totalMin(groups)
    

    # sol 2:
    # runtime: 46ms
    def totalMin(A):
        ans, i, j = 0, 0, len(A)-1
        while i < j:
            ans += A[j] - A[i]
            i += 1
            j -= 1
        return ans
    n, m = len(grid), len(grid[0])
    groups = [(i,j) for i in range(n) for j in range(m) if grid[i][j]!=0]
    I, J = sorted([x[0] for x in groups]), sorted([x[1] for x in groups])
    return totalMin(I) + totalMin(J)

    # sol 3:
    # not use sort(), use two pointers.
    # runtime: 37ms
    rowsum = map(sum, grid)
    colsum = map(sum, zip(*grid))
    def totalMin(A):
        i, j = -1, len(A)
        res = left = right = 0
        while i < j:
            if left < right:
                res += left
                i += 1
                left += A[i]
            else:
                res += right
                j -= 1
                right += A[j]
        return res
    return totalMin(rowsum) + totalMin(colsum)


    # sol 3:
    # no sorting involved
    # runtime:






