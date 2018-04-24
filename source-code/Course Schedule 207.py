# 207. Course Schedule
# ttungl@gmail.com
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# For example:
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, 
# and to take course 0 you should also have finished course 1. So it is impossible.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # sol 1
        # BFS topological sort
        # time O(V+E) space O(V+E)
        # runtime: 46ms
        #
        # construct a graph
        graph = [[] for _ in range(numCourses)]
        visit = [0]*numCourses
        for i,j in prerequisites:
            graph[j].append(i)
            visit[i] += 1
        # search nodes with not have been visited yet and put into queue.
        queue = collections.deque()
        for i in range(numCourses):
            if visit[i] == 0:
                queue.append(i)
        # find whether it's possible to take all courses.
        k = 0
        while queue:
            node = queue.popleft()
            k += 1
            for i in graph[node]:
                visit[i] -= 1
                if visit[i] == 0:
                    queue.append(i)
        return k == numCourses


        # sol 2
        # Use DFS backtracking
        # runtime: 58ms
        # time: O(V*E)
        # space: O(V*E)

        # construct a graph
        graph = [[] for _ in range(numCourses)]
        [graph[x].append(y) for x, y in prerequisites]
        visit = [0]*numCourses
        
        def DFS(i):
            if visit[i] == -1: 
                return False # if -1 in visit, it's a ring.
                
            elif visit[i] == 1: 
                return True # if 1 in visit, there's no ring contain node v and its successor. 

            visit[i] = -1 # being visited

            for j in graph[i]:
                if not DFS(j): 
                    return False

            visit[i] = 1 # has been visited
            return True
        
        for i in range(numCourses):
            if not DFS(i): 
                return False
        return True








