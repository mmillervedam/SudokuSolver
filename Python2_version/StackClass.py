"""
Stack class
"""

class Stack:
    """
    A simple implementation of a LIFO stack.
    """

    def __init__(self):
        """ 
        Initialize the stack.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the stac.
        """
        return len(self._items)
    
    #def __iter__(self):
        #"""
        #Create an iterator for the stack.
        #"""
        #for item in self._items:
            #yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def push(self, item):
        """
        Add item to the stack.
        """        
        self._items.append(item)

    def pop(self):
        """
        Remove and return the most recently inserted item.
        """
        return self._items.pop()

    def clear(self):
        """
        Remove all items from the stack.
        """
        self._items = []
        
