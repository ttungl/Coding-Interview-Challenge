# 781. Rabbits in Forest

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        # sol 1:
        # v rabbits answered k.
        # v = count[k]
        # runtime: 51ms
        count = collections.Counter(answers)
        return sum(-v%(k+1) + v for k, v in count.iteritems())
    
        # sol 2:
        # runtime: 54ms
        # put every rabbit with the same key (answer) into the same group 
        # as much as possible.
        # The number of the subgroup is computed from ceil(1.0 x cnt/key), 
        # so the total number of all these subgroups under the same key is 
        # ceil(1.0 x cnt/key) x key.
        count = collections.Counter(answers)
        return sum((count[i] + i)/(i+1)*(i+1) for i in count)
        
        
