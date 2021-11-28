class Stack():
    def __init__(self):
        self.stack = []
        pass

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return f'Стэк пуст'
        deleted = self.stack.pop()
        return deleted

    def peek(self):
        if self.isEmpty():
            raise f'Стэк пуст'
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)