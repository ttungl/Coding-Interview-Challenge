# 815. Bus Routes
# ttungl@gmail.com
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

# We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

# Example:
# Input: 
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation: 
# The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Note:

# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        # sol 1:
        # BFS
        # time O(V*ElogV) space O(V)
        # runtime: 2593ms
        queue = [(S, 0)] # (bus_stop, #buses)
        visited = set([S]) # visited bus stops/routes
        d = collections.defaultdict(set) # map[key, val]~[bus stop, route id]

        for i, route in enumerate(routes): 
            for j in route: # each bus stop
                d[j].add(i) 

        for stop, numBuses in queue:
            if stop == T: 
            	return numBuses
            for route_id in d[stop]:
                for next_stop in routes[route_id]:
                    if next_stop not in visited:
                        queue.append((next_stop, numBuses + 1))
                        visited.add(next_stop)
        return -1
                
                