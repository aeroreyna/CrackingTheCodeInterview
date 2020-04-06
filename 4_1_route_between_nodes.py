class node:
    def __init__(self, value):
        self.v = value
        self.adjacent = []
        self.visited = False


class Graph:
    def __init__(self):
        self.nodes = []

    def add(self, v):
        self.nodes.append(node(v))
        return self.nodes[-1]


class Queue:  # Not Efficeint Queue
    def __init__(self):
        self.a = []

    def push(self, a):
        self.a.extend(a)

    def unqueue(self):
        return self.a.pop(0)

    def is_empty(self):
        return len(self.a) == 0


def route_between_nodes(n1, n2):  # Breath-First-Search
    s = Queue()
    if not n1 or len(n1.adjacent) == 0:
        return False
    s.push(n1.adjacent)
    while not s.is_empty():
        n = s.unqueue()
        if n.visited:
            continue
        n.visited = True
        if(n == n2):
            return True
        s.push(n.adjacent)
    return False


def route_between_nodes_DFS(n1, n2):  # Depth-First-Search
    if n1.visited:
        return False
    if n1 == n2:
        return True
    n1.visited = True
    for n in n1.adjacent:
        if(route_between_nodes_DFS(n, n2)):
            return True
    return False


if __name__ == '__main__':
    g = Graph()
    n0 = g.add(0)
    n1 = g.add(1)
    n2 = g.add(2)
    n3 = g.add(3)
    n4 = g.add(4)
    n5 = g.add(5)
    n0.adjacent.extend([n1, n4, n5])
    n1.adjacent.extend([n4, n3])
    n2.adjacent.extend([n1])
    n3.adjacent.extend([n2, n4])

    print(route_between_nodes_DFS(n0, n2))  # True
