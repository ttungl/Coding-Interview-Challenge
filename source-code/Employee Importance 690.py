# 690. Employee Importance



"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # sol 1:
        # runtime: 269ms
        em = {e.id: e for e in employees}
        def dfs(id):
            return sum(dfs(j) for j in em[id].subordinates) + em[id].importance
        return dfs(id)
    
        # sol 2:
        # runtime: 352ms
        emp = {e.id: e for e in employees}
        res=0
        st = [emp[id]] # go to employee id with a map emp. 
        while st:
            s = st.pop()
            res+= s.importance
            [st.append(emp[i]) for i in s.subordinates]
        return res
        
        
            
        