class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []  # True or False

    def push(self, item):
        self.items.append(item)  # Add new item.

    def pop(self):
        return self.items.pop()  # Cut last item.

    def peek(self):
        return self.items[len(self.items) - 1]  # Read last item.

    def size(self):
        return len(self.items)  # Size of items.
stack = Stack()

for c in "Hello":
    stack.push(c)

reverse = ""

while stack.size():
    reverse += stack.pop()  # "+=" run add each letter in case of str data.
    # reverse = reverse + stack.pop()

print(reverse)
