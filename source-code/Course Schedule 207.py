# 207. Course Schedule

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
        # Use DFS backtracking
        # runtime: 58ms
        # time: O(n^2)
        # space: O(n)

        graph = [[] for _ in range(numCourses)]

        [graph[x].append(y) 
            for x, y in prerequisites]

        visit = [0]*numCourses
        
        def DFS(i):
            if visit[i] == -1: return False # if -1 in visit, it's a ring.
            elif visit[i] == 1: return True # if 1 in visit, there's no ring contain node v and its successor. 

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
