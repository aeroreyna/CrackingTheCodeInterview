class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.v = v


def list_of_depths(n):
    def childs_arr(n):
        a = []
        if n.left:
            a.append(n.left)
        if n.right:
            a.append(n.right)
        return a
    h = {}
    h[1] = n
    next = childs_arr(n)
    depth = 2
    while len(next):
        h[depth] = next
        temp = []
        for i in range(len(next)):
            temp.extend(childs_arr(next[i]))
        next = temp
        depth += 1
    return h


def list_of_depths_rec(n, h={}, d=1):
    if not n:
        return h
    if n.left:
        list_of_depths_rec(n.left, h, d+1)
    if n.right:
        list_of_depths_rec(n.right, h, d+1)
    if d not in h:
        h[d] = []
    h[d].append(n)
    return h


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n1.left = n2
    n2.left = n4
    n2.right = n5
    n1.right = n3
    n3.left = n6
    n6.left = n8
    n6.right = n9
    n9.right = n10
    n3.right = n7
    print(list_of_depths_rec(n1))
