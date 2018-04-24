# 146. LRU Cache
# ttungl@gmail.com
class LRUCache(object):

    # sol 1: use collections.OrderedDict()
    # runtime: 322ms
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.remain = capacity
        self.dic = collections.OrderedDict() # remembers the order entries were added

    def get(self, key):
        if key not in self.dic:
            return -1
        val = self.dic.pop(key)
        self.dic[key] = val # update key as newest one.
        return val
        
    def put(self, key, value):
        # Set or insert the value if the key is not already present. 
        # When the cache reached its capacity, 
        # it should invalidate the least recently used item before inserting a new item.
        if key in self.dic:
            self.dic.pop(key)
        else: # insert value 
            if self.remain > 0: self.remain -= 1
            else: # when cache (self.dic) is full
                # popitem() returns and removes a (key, value) pair.
                # The pairs are returned in LIFO order if last is true or FIFO order if false.
                self.dic.popitem(last=False) # FIFO
        self.dic[key] = value
            
    # sol 2: use dictionary and deque().
    # runtime: 879ms
    def __init__(self, capacity):
        self.remain = capacity
        self.dic = {}
        self.deque = collections.deque([])
        
    def get(self, key):
        if key not in self.dic: return -1
        self.deque.remove(key)
        self.deque.append(key)
        return self.dic[key]
    
    def put(self, key, value):
        if key in self.dic:
            self.deque.remove(key)
        elif self.remain == len(self.dic):
            val = self.deque.popleft() # remove LRU element
            self.dic.pop(val)
        self.deque.append(key)
        self.dic[key] = value
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


















# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)