class stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0