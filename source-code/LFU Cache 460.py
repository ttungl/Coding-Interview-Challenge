# 460. LFU Cache

class LFUCache(object):
    
    # --
    # LFU (Least Frequently Used) is a famous cache eviction algorithm.
    # For a cache with capacity k, if the cache is full and need to evict a key in it, 
    # the key with the lease frequently used will be kicked out.
    # =
    # Use OrderedDict() with O(1) time.
    # nodesForFrequency stores the mapping from frequency to OrderedDict with key => (value, frequency).
    # For example, after these three operations: put(1,1), put(2,2), get(1), put(3,3) the nodesForFrequency will be:
    #      frequency  => { key  => (value, frequency), ...        }
    # {
    #      1          => { 2    => (2    , 1),         3 =>(3, 1) },
    #      2          => { 1    => (1    , 2)                     }
    # }
    # --
    # runtime: 375ms
    # --
    def __init__(self, capacity):
        self.remain = capacity 
        self.nodesForFrequency = collections.defaultdict(collections.OrderedDict) # keeps track of key => (val,freq)
        self.leastFrequency = 1 
        self.nodeForKey = {} # cache; (val, freq)
        
        
    def _update(self, key, newValue=None):
        value, freq = self.nodeForKey[key] # get (value, frq) from cache[key]
        if newValue is not None: 
            value = newValue
        self.nodesForFrequency[freq].pop(key) # pop the key with least frequency used at index freq.
        # freq_tracker at index freq is empty, increase freq by 1.
        if len(self.nodesForFrequency[self.leastFrequency]) == 0: 
            self.leastFrequency += 1
        # update cache and freq_tracker with (val,freq+1)
        self.nodesForFrequency[freq+1][key] = (value, freq+1) 
        self.nodeForKey[key] = (value, freq+1)
        
    def get(self, key):
        if key not in self.nodeForKey: 
            return -1
        self._update(key)
        return self.nodeForKey[key][0]
        
    def put(self, key, value):
        if key in self.nodeForKey: self._update(key, value)
        else:
            # update key to cache and frequency tracker.
            self.nodeForKey[key] = (value,1) # (val, freq)
            self.nodesForFrequency[1][key] = (value,1)
            # check cache capacity
            if self.remain == 0:
                removed = self.nodesForFrequency[self.leastFrequency].popitem(last=False) # FIFO for frequency tracker
                self.nodeForKey.pop(removed[0]) # cache
            else: 
                self.remain -= 1
            self.leastFrequency = 1 # should be one after adding a new item
            
            
        
        
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)