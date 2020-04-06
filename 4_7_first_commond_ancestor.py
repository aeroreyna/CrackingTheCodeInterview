class node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.v = v


def FCA_internet(n, q, p):  # First Commond Ancestor of values q and p
    # This not considers the case on which either q or p are not in the tree
    if not n:
        return n
    if n.v == q or n.v == p:
        return n
    left = FCA_internet(n.left, q, p)
    right = FCA_internet(n.right, q, p)
    if (left.v == q and right.v == p) or (left.v == p and right.v == q):
        return n  # found it
    return left if left else right  # Carried the non false value to the top


def path_to_node(n, q, path):
    if not n:
        return n
    if n.v == q:
        path.enqueue(n)
        return path
    if path_to_node(n.left, q, path) or path_to_node(n.right, q, path):
        path.enqueue(n)
        return path
    return False


def LCA(n, q, p):
    path1 = path_to_node(n, q)
    path2 = path_to_node(n, p)
    if not (path1 and path2):
        return False
    i = 0
    while path1[i] == path2[i]:
        i += 1
    return path1[i-1]


if __name__ == '__main__':
    
