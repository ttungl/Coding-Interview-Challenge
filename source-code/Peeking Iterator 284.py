284. Peeking Iterator

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

Follow up: How would you extend your design to be generic and work with all types, not just integer?

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    # sol 1:
    # runtime: 55ms
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nums = iterator
        self.cur = self.nums.next() if self.nums.hasNext() else None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cur

    def next(self):
        """
        :rtype: int
        """
        res = self.cur
        self.cur = self.nums.next() if self.nums.hasNext() else None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur is not None 

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


class PeekingIterator(object):
 	# sol 2
    # runtime: 39ms
    def __init__(self, iterator):
        self.iter = iterator
        self.has_next = self.iter.hasNext()
        self.cur = self.iter.next() if self.has_next else None
        
    def peek(self):
        return self.cur
        
    def next(self):
        res = self.cur
        self.has_next = self.iter.hasNext()
        self.cur = self.iter.next()
        return res
        
    def hasNext(self):
        return self.has_next


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].























