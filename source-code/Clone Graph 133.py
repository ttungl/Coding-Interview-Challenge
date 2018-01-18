# 133. Clone Graph 133

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def __init__(self):
        self.visited = {}
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        
        # sol 1
        # use BFS (queue)
        # time O(n^2)
        # space O(n)
        # runtime: 72ms
        if not node: 
        	return node
        
        root = UndirectedGraphNode(node.label)
        
        queue, visit = [node], {}
        
        visit[node.label] = root

        while queue:
            top = queue.pop()
            for n in top.neighbors:
                if n.label not in visit:
                    queue.append(n)
                    visit[n.label] = UndirectedGraphNode(n.label)

                visit[top.label].neighbors.append(visit[n.label])
        
        return root
        
        # sol 2:
        # use DFS
        # runtime: 79ms
        # time: O(n^2)
        # space: O(n)
        if not node: 
            return node
        
        if node.label in self.visited:
            return self.visited[node.label]
        
        clone = UndirectedGraphNode(node.label)
        
        self.visited[node.label] = clone
        
        [clone.neighbors.append(self.cloneGraph(n)) for n in node.neighbors]
        
        return clone
        
        # sol 3
        # use DFS (stack)
        # runtime: 122ms
        # time: O(n^2)
        # space: O(n)
        def DFS(node, visited):
            if node in visited:
                return visited[node]

            clone = UndirectedGraphNode(node.label)
            
            visited[node] = clone
            
            [clone.neighbors.append(DFS(x, visited)) for x in node.neighbors]
            
            return clone
        
        if not node: 
            return node

        return DFS(node, {})
        
        # sol 4
        # use BFS (queue)
        # runtime: 95ms
        # time: O(n^2)
        # space: O(n)
        def BFS(node, visited, queue):
            clone = UndirectedGraphNode(node.label)
            visited[node] = clone 

            while queue:
                top = queue.pop()
                for nb in top.neighbors:
                    if nb not in visited: # neighbor not in visited dictionary
                        clonecp = UndirectedGraphNode(nb.label)
                        visited[nb] = clonecp
                        visited[top].neighbors.append(clonecp)
                        queue.append(nb)
                    else:    
                        visited[top].neighbors.append(visited[nb])
            
            return clone
        
        if not node: 
        	return node
        
        visited, queue = {}, [node]
        
        return BFS(node, visited, queue)
        
        
        
        
        
