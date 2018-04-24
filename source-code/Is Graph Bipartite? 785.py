# 785. Is Graph Bipartite?
# ttungl@gmail.com

# Given a graph, return true if and only if it is bipartite.

# Recall that a graph is bipartite if we can split it's set of nodes 
# into two independent subsets A and B such that every edge in the 
# graph has one node in A and another node in B.

# The graph is given in the following form: graph[i] is a list of 
# indexes j for which the edge between nodes i and j exists.  
# Each node is an integer between 0 and graph.length - 1. 
# There are no self edges or parallel edges: graph[i] does not 
# contain i, and it doesn't contain any element twice.

# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation: 
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.

# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
# Output: false
# Explanation: 
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent ubsets.


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # sol 1:
        # use coloring graph.
        # runtime: 90ms
        def dfs(node, cur):
            if node in visited: return visited[node] == cur
            visited[node] = cur
            return all(dfs(n, not cur) for n in graph[node])
        visited = collections.defaultdict(int)
        return all(dfs(n, 0) for n in range(len(graph)) if n not in visited)
    
        # sol 2:
        # runtime: 66ms
        def dfs(node, cur):
            if node in visited:
                return visited[node]==cur
            visited[node]=cur
            return all(dfs(node, not cur) for node in graph[node])
        visited = {}
        return all(dfs(n, 0) for n in range(len(graph)) if n not in visited)
    
        # sol 3:
        # runtime: 68ms
        def dfs(n):
            for i in graph[n]:
                if i in visited:
                    if visited[i]==visited[n]: return False
                else: 
                    visited[i] = 1-visited[n]
                    if dfs(i)^1: return False
            return True
        visited = {}
        for i in range(len(graph)):
            if i not in visited: visited[i]=0
            if dfs(i)^1: return False
        return True
    
    
    




