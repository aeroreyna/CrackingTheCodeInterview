class Node:
    def __init__(self, v):
        self.v = v
        self.next = None
        self.min = self


class Stack:
    def __init__(self):
        self.head = None

    def push(self, v):
        n = Node(v)
        n.next = self.head
        if self.head and (self.head.min.v < n.min.v):
            n.min = self.head.min
        self.head = n
        return self

    def pop(self):
        n = self.head
        if self.head:
            self.head = self.head.next
        return n

    def min(self):
        if self.head:
            return self.head.min
        return None


if __name__ == '__main__':
    s = Stack()
    s.push(10).push(11).push(10).push(5).push(7).push(8)
    for i in range(6):
        n = s.pop()
        print("current {}, min {}".format(n.v, n.min.v))
