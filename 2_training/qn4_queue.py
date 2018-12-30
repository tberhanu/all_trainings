#!/usr/bin/env python3

class Queue(object):
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enqueue(self,element):
        self.stack1.append(element)
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__ == "__main__":
    q=Queue()
    for i in range(5):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())
    for i in range(3):
        q.enqueue(i + 100)
    for i in range(3):
        print(q.dequeue())
