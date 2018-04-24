# 323. Number of Connected Components in an Undirected Graph
# ttungl@gmail.com
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

# Example 1:
#      0          3
#      |          |
#      1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

# Example 2:
#      0           4
#      |           |
#      1 --- 2 --- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

# Note:
# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and 
# thus will not appear together in edges.

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # sol 1:
        # BFS
        # 1. convert edges to adjacent list of the graph
        # 2. keep track of visited nodes
        # 3. use stack to perform DFS.
        # time O(V+E) space O(V)
        # runtime: 70ms
        graph = {i:set() for i in range(n)} # create sets for each node/vertex.
        for i, j in edges: # assign edges to the adjacent list.
            graph[i].add(j)
            graph[j].add(i)
        visited, stack, count = set(), [], 0 # visited nodes; stack dfs and count #components.
        for i in range(n): 
            if i not in visited: # if node is not visited yet, it belongs to a component, so count it.
                count+=1
                stack.append(i) 
                while stack: 
                    top = stack.pop()
                    visited.add(top)
                    [stack.append(node) for node in graph[top] if node not in visited] # add all nodes that connect to node "top" in graph to the stack.
        return count
        
        
        # sol 2
        # DFS
        # 1. convert edges list to adjacent list
        # 2. keep track nodes visited on visited list, 
        # recursive if node is not visited yet.
        # time O(V+E) space O(V)
        # runtime: 67ms
        # DFS
        def dfs(graph, i, visited):
            for j in graph[i]: # check adjacent nodes.
                if j not in visited:
                    visited.add(j)
                    dfs(graph, j, visited)
        visited, count = set(), 0
        graph = {i:set() for i in range(n)} #.1
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        for i in range(n): #.2
            if i not in visited:
                visited.add(i)
                count+=1
                dfs(graph, i, visited)
        return count
        
        
        # sol 3
        # union find
        # runtime: 67ms
        # credit to https://discuss.leetcode.com/topic/84031/python-union-find
        roots = range(n)
        graph = {i:set() for i in range(n)}
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        for i,j in edges:
            x, y = roots[i], roots[j]
            if x==y: 
                continue
            lx, ly = len(graph.get(x, [])), len(graph.get(y, []))
            if lx < ly: 
                x, y = y, x
            graph[x] |= graph[y]
            for i in graph.pop(y, []):
                roots[i] = x
        return len(graph)


        
        
        
        

