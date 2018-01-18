# 765. Couples Holding Hands


class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        # sol: use dictionary
        # to store key(num) and value(index)
        # time O(n) space O(n)
        # runtime: 36ms
        # --
        count = 0
        # key v (number): value i (index)
        d = {value:index for index, value in enumerate(row)} 
        for i in range(len(row)):
            num = row[i]
            if num % 2 == 0: ans = num+1
            else: ans = num-1
            j = d[ans]
            if j-i > 1:
                row[i+1], row[j] = row[j], row[i+1]
                d[row[i+1]] = i+1
                d[row[j]] = j
                count+=1
        return count