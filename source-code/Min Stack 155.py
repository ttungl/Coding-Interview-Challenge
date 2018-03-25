# 155. Min Stack

class MinStack(object):
	# using list array
    # runtime: 72 ms
    def __init__(self):
        self.stack = []

    def push(self, x):
    	if not self.stack: 
            self.stack.append((x, x))
    	else:
        	self.stack.append((x, min(x, self.stack[-1][1]))) # keep track on x and min.

    def pop(self):
    	if self.stack:
        	self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return None
        

    #################################################
    # sol 2:
    # keep stack and min in the separate lists.
    # runtime: 79ms
    def __init__(self):
        self.stack = list()
        self.minlist = list()
        
    def push(self, x):
        self.stack.append(x)
        if not self.minlist: self.minlist.append(x)
        else: 
            self.minlist.append(min(x, self.minlist[-1]))

    def pop(self):
        if self.stack:
            del self.stack[-1]
            del self.minlist[-1]

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minlist[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

