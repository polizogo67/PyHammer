class Node(object):

    def __init__(self, data=None, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def next(self):
        return self._next_node

    @next.setter
    def next(self, value: 'Node') -> None:
        self._next_node = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value) -> None:
        self._data = value


class LinkedList(object):

    def __init__(self, root=None):
        self._root = root
        self._size = 0

    @property
    def size(self):
        return self._size

    def push_back(self, data):
        if self._root is None:
            self._root = Node(data, None)
            self._size += 1
            return

        current = self._root
        while current.next is not None:
            current = current.next

        current.next = Node(data, None)
        self._size += 1

    def push_front(self, data):
        new_node = Node(data, self._root)
        self._root = new_node
        self._size += 1