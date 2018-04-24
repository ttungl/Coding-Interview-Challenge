# 261. Graph Valid Tree
# ttungl@gmail.com
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
# (each edge is a pair of nodes), write a function to check whether these 
# edges make up a valid tree.

# For example:
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Note: you can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and 
# thus will not appear together in edges.

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """ 
        # sol1: DFS
        # time O(n) space O(n)
        # runtime: 53ms
        visited, stack = set(), [0]
        graph = {i:set() for i in range(n)}
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        while stack: 
            top = stack.pop()
            if top in visited: # acyclic detected!
                return False 
            visited.add(top) # v=(0)
            stack.extend(graph[top] - visited) # **^remove same #s in visited; 
        return len(visited) == len(graph) # len(graph) = n
    
        # sol2: DFS
        # time O(n) space O(n)
        # runtime: 72ms
        graph = {i:set() for i in range(n)}
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        def visited(v):
            map(visited, graph.pop(v, [])) # map(function_call, list_of_inputs)
        visited(0)
        return len(edges)==(n-1) and not graph
        
        # sol3: BFS
        # time O(n) space O(n)
        # runtime: 65ms
        graph = {i:set() for i in range(n)}
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        queue = collections.deque([0])
        while queue:
            queue.extend(graph.pop(queue.popleft(), []))
        return len(edges)==(n-1) and not graph
        
        
        # sol4: union find
        # time O(n) space O(n)
        # runtime 41ms
        root = range(n)
        def find(x):
            return x if root[x]==x else find(root[x])
        def union(xny):
            x, y = map(find, xny)
            root[x] = y
            return x!=y
        return len(edges)==n-1 and all(map(union, edges)) 










                
                        
        
