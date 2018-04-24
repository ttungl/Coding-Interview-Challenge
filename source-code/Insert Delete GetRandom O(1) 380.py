# Insert Delete GetRandom O(1) 380
# runtime: 162ms
# ttungl@gmail.com
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = [] # list: makes sure insert() and getRandom is O(1)
        self.dict = {} # dict: makes sure remove() is O(1). It maps the values to their indices in the list, so we can quickly remove sth from it.
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        
        # swap
        x, y = self.dict[val], self.list[-1] # key in dict and last element in list.
        self.list[x], self.dict[y] = y, x
        
        # delete val
        del self.dict[val]
        self.list.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()