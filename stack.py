MAXIMUM_STACK_SIZE = 1024
class Stack:
    def __init__(self):
        self.items = []
    def __str__(self):
        ws = []
        for i, item in enumerate(self.items):
            if i == 0:
                ws.append(f"{item} <first")
            elif i == len(self.items) - 1:
                ws.append(f"{item} <last")
            else:
                ws.append(str(item))
        return "\n".join(ws)
    def push(self, item):
        if self.size() == MAXIMUM_STACK_SIZE:
            raise Exception("Stack overflow: maximum stack size reached")
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self, depth=0):
        if depth < 0:
            raise ValueError("depth must be non-negative")
        if depth >= self.size():
            raise IndexError("peek depth exceeds stack size")
        return self.items[-(depth + 1)]

    @property
    def stack(self):
        return self.items.copy()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)