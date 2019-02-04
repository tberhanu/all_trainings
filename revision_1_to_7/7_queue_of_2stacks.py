"""
7. Make a Queue calss using 2 stacks, so that you implement enqueue and dequeue method,
and run it with example.
"""

class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, e):
        self.stack1.append(e)

    def dequeue(self):

        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())