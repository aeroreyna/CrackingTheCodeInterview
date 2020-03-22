class Node:
    def __init__(self, v):
        self.v = v
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, v):
        n = Node(v)
        n.next = self.head
        self.head = n
        return self

    def pop(self):
        n = self.head
        if self.head:
            self.head = self.head.next
        return n and n.v


class Queue:
    def __init__(self):
        self.s = Stack()
        self.size = 0

    def queue(self, v):
        self.s.push(v)
        self.size += 1
        return self

    def unqueue(self):
        if not self.s.head:
            return False
        new_s = Stack()
        while self.s.head is not None:
            new_s.push(self.s.pop())
        return_v = new_s.pop()
        while new_s.head is not None:
            self.s.push(new_s.pop())
        self.size -= 1
        return return_v

    def unqueue_n(self, n):
        if not self.s.head:
            return False
        new_s = Stack()
        while self.s.head is not None:
            new_s.push(self.s.pop())
        return_v = []
        for i in range(n):
            return_v.append(new_s.pop())
        while new_s.head is not None:
            self.s.push(new_s.pop())
        self.size -= n
        if self.size < 0:
            self.size = 0
        return return_v


if __name__ == '__main__':
    q = Queue()
    for i in range(20):
        q.queue(i)
    for i in range(10):
        print(q.unqueue())
    for i in range(2):
        print(q.unqueue_n(8))  # [10, 11, 12, 13, 14]
                               # [15, 16, 17, 18, 19]
    print(q.size)
