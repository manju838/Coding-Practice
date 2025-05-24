class Stack:
    def __init__(self):
        self.items = [] # Initialise an empty arraylist to store stack items

    def is_empty(self):
        return len(self.items) == 0

    # Common stack operations
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)