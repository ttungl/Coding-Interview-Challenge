# 716. Max Stack


class MaxStack(object):

	# sol :
	# runtime: 269 ms
    def __init__(self):
        self.stack = []
        self.maxlist = []
    
    def push(self, x):
        self.stack.append(x)
        if not self.maxlist: 
            self.maxlist.append(x)
        else:
            self.maxlist.append(max(x, self.maxlist[-1]))
    
    def pop(self):
        self.maxlist.pop()
        return self.stack.pop()
    
    def top(self):
        if self.stack: 
        	return self.stack[-1]
        
    def peekMax(self):
        return self.maxlist[-1]

    def popMax(self):
        n = self.maxlist.pop()
        i = len(self.stack)-1
        tmp = []
        while n != self.stack[-1]: 
            tmp.append(self.pop())
        res = self.stack.pop()
        [self.push(tmp[i]) for i in range(len(tmp)-1,-1,-1)]
        return res



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()