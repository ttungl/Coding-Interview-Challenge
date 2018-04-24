# 797. All Paths From Source to Target
# ttungl@gmail.com

# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# Note:

# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of nodes inside one path.

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # sol 1:
        # DFS: time O(n) space O(n)
        # runtime: 336ms
        def dfs(idx, path):
            if idx == len(graph)-1:
                res.append(path)
            for i in graph[idx]:
                dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res
        
        # sol 2:
        # iterative 
        # runtime: 341ms
        res, path, lenGraph = [], [0], len(graph)
        stack = [(0, [0])]
        while stack:
            idx, path = stack.pop()
            if idx == (lenGraph - 1):
                res.append(path)
            for i in graph[idx]:
                stack.append((i,path+[i]))
        return res



        

