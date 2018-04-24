# 802. Find Eventual Safe States
# ttungl@gmail.com

# In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

# Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

# Which nodes are eventually safe?  Return them as an array in sorted order.

# The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

# Example:
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Here is a diagram of the above graph.

# Illustration of graph

# Note:

# graph will have length at most 10000.
# The number of edges in the graph will not exceed 32000.
# Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # sol 1:
        # use DFS
        # runtime: 292ms
        # states:
        # 0: not visited yet
        # 1: safe (walk to terminal)
        # 2: unsafe (visited, to a cycle)
        def dfs(graph, cur, states):
            if states[cur] != 0:
                return states[cur]==1
            states[cur] = 2 # visited (unsafe)
            for j in graph[cur]: # check cycle
                if not dfs(graph, j, states):
                    return False
            states[cur] = 1 # eventually safe.
            return True
        #
        res = []
        states = [0]*len(graph)
        for i in range(len(graph)):
            if dfs(graph, i, states):
                res.append(i)
        return res
        
        # sol 2:
        # find nodes that don't lead to a cycle in any paths.
        # use BFS
        # runtime: 476ms
        res, queue = [], []
        outdict = collections.defaultdict(int)
        indict = collections.defaultdict(list)
        for i in range(len(graph)):
            outdict[i] = len(graph[i])
            if outdict[i] == 0:
                queue.append(i)
            [indict[j].append(i) for j in graph[i]]
        #
        while queue:
            tmp = queue.pop(0) 
            res.append(tmp)
            for j in indict[tmp]:
                outdict[j] -= 1
                if outdict[j] == 0:
                    queue.append(j)
        return sorted(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    





