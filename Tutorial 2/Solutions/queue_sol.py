""" Queue class
"""


class Queue:
    """
    A first-in, first-out (FIFO) queue.
    """

    def __init__(self):
        """
        Create and initialize new Queue self.

        @param Queue self: this queue
        @rtype: None
        """
        self._data = []

    def add(self, obj):
        """
        Add object at the back of Queue self.

        @param Queue self: this queue
        @param object obj: object to add
        @rtype: None
        """
        self._data.append(obj)

    def remove(self):
        """
        Remove and return front object from Queue self.

        Queue self must not be empty.

        @param Queue self: this Queue
        @rtype: object

        >>> q = Queue()
        >>> q.add(3)
        >>> q.add(5)
        >>> q.remove()
        3
        """
        return self._data.pop(0)

    def is_empty(self):
        """
        Return whether Queue self is empty

        @param Queue self:
        @rtype: bool

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        >>> q.remove()
        5
        >>> q.is_empty()
        True
        """
        return self._data == []


if __name__ == '__main__':
    import doctest
    doctest.testmod()
