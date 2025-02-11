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

    def __repr__(self):
        return f"Node({self._data})"


class LinkedList(object):

    def __init__(self, root=None):
        self._root = root
        self._size = 0

    @property
    def size(self):
        return self._size

    def push(self, data):
        new_node = Node(data, self._root)
        self._root = new_node
        self._size += 1

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

    def insert(self, index, data) -> bool:
        if index > self._size:
            return False

        if index == 0:
            self.push(data)
            return True

        current = self._root
        for i in range(index - 1):
            current = current.next

        new_node = Node(data, current.next)
        current.next = new_node
        self._size += 1

    def get(self, index):
        if index >= self._size:
            return None

        current = self._root
        for i in range(index):
            current = current.next

        return current

    def pop(self):
        if self._root is None:
            return None

        data = self._root.data
        self._root = self._root.next
        self._size -= 1

        return data

    def count(self):
        count = 0
        current = self._root
        while current is not None:
            count += 1
            current = current.next
        return count