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


def sort_stack(s):
    ordered = Stack()
    ordered.push(s.pop())
    while s.head:
        temp = s.pop()
        if temp < ordered.head.v:
            ordered.push(temp)
        else:
            while ordered.head:
                s.push(ordered.pop())
            ordered.push(temp)
    return ordered


if __name__ == '__main__':
    s = Stack()
    s.push(10).push(15).push(2).push(7).push(14)
    s = sort_stack(s)
    while s.head:
        print(s.pop())
