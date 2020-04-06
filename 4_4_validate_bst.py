class Node():
    def __init__(self, v):
        self.left = None
        self.right = None
        self.v = v


def validate_bst(n):
    if not n:
        return True
    if n.left and n.v < n.left.v:
        return False
    if n.right and n.v >= n.right.v:
        return False
    if not (validate_bst(n.left) and validate_bst(n.right)):
        return False
    return True


if __name__ == '__main__':
    n10 = Node(10)
    n7 = Node(7)
    n4 = Node(4)
    n8 = Node(8)
    n15 = Node(15)
    n12 = Node(12)
    n11 = Node(11)
    n16 = Node(16)
    n17 = Node(17)
    n10.left = n7
    n7.left = n4
    n7.right = n8
    n10.right = n15
    n15.left = n12
    n12.left = n11
    n15.right = n16

    print(validate_bst(n10))
    n16.left = n17
    print(validate_bst(n10))
