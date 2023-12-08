class Stack:
    def __init__(self, items=None):
        self.items = []
        self.limit =  [] if items is None else items[:]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def is_full(self):
        return self.limit is not None and len(self.items) == self.limit

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
             return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def search(self, value):
        if value in self.items:
            return len(self.items) - self.items.index(value) - 1
        return -1

