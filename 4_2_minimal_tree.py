import math


class bin_node:
    def __init__(self, value):
        self.v = value
        self.left = None
        self.right = None


def construct_binary_search_tree(a):
    if len(a) == 0:
        return None
    if len(a) == 1:
        return bin_node(a[0])
    middle = math.floor(len(a)/2)
    n = bin_node(a[middle])
    n.left = construct_binary_search_tree(a[:middle])
    n.right = construct_binary_search_tree(a[middle+1:])
    return n


def tree_in_order(n):
    if not n:
        return 0
    if n.left:
        tree_in_order(n.left)
    print(n.v)
    if n.right:
        tree_in_order(n.right)
    return 0


def tree_height(n):
    if not n:
        return 0
    return max(tree_height(n.left), tree_height(n.right)) + 1


if __name__ == '__main__':
    a = list(range(1023))
    head = construct_binary_search_tree(a)
    tree_in_order(head)
    print("height:", tree_height(head))
