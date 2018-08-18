class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)  # "insert" not "append"

    def dequeue(self):
        return self.items.pop()  # same as stack

    # def peek(self):
    #     return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

queue = Queue()

print(queue.is_empty())

for i in range(5):  # 0 ~ 4
    queue.enqueue(i)

while queue.size():
    print(queue.dequeue())  # 0, 1, 2, 3, 4 (not from the last)

print()
print(queue.size())
