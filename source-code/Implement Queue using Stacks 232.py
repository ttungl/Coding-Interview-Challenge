# 232. Implement Queue using Stacks

class MyQueue(object):
    # The idea is to simulate a queue using two stacks (same as previous posts). 
    # Use python list as the underlying data structure for stack and add a "move()" method to simplify code: 
    # it moves all elements of the "stackin" to the "stackout" when the "stackout" is empty. 
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackin, self.stackout = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stackin.append(x)
            
            
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move() # move all elements from stackin to stackout
        self.stackout.pop()

        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move()
        self.stackout[-1]
        
        
    def move(self):
        """ move all elements from stackin to stackout """
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
        
        
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stackin)==0 and len(self.stackout)==0
    
    
    
    
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
