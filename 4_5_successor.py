class Node():
    def __init__(self, v):
        self.left = None
        self.right = None
        self.parent = None
        self.v = v

    def add_left(self, n=None):
        if not n:
            return n.left
        self.left = n
        n.parent = self

    def add_right(self, n=None):
        if not n:
            return n.left
        self.right = n
        n.parent = self


def min_of_bst(n):
    if not n:
        return n
    while n.left:
        n = n.left
    return n


def successor(n):
    if not n:
        return n
    if n.right:
        return min_of_bst(n.right)
    while n.parent:
        if n.parent.left == n:
            return n.parent
        n = n.parent
    return None


if __name__ == '__main__':
    n10 = Node(10)
    n7 = Node(7)
    n4 = Node(4)
    n8 = Node(8)
    n15 = Node(15)
    n12 = Node(12)
    n11 = Node(11)
    n16 = Node(16)
    n10.add_left(n7)
    n7.add_left(n4)
    n7.add_right(n8)
    n10.add_right(n15)
    n15.add_left(n12)
    n12.add_left(n11)
    n15.add_right(n16)

    print(successor(n8).v)
