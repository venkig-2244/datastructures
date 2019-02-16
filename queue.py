class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items) > 0:
            self.items.pop()

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        if len(self.items) > 0:
            return False

        return True


