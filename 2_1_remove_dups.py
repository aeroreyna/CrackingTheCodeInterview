class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        n = self
        str = "{}".format(n.value)
        while n.next:
            n = n.next
            str += "->{}".format(n.value)
        return str

    def push(self, value):
        n = self
        while n.next:
            n = n.next
        n.next = Node(value)
        return n.next


def remove(n):
    if(not n.next):
        return False
    n.value = n.next.value
    n.next = n.next.next
    return True


def remove_dups(n):
    dict = {}
    if not n or not n.next:
        return n

    def in_dict(v):
        if v in dict:
            return True
        dict[v] = 1
        return False
    in_dict(n.value)
    prev = n
    n = n.next
    while n:
        if in_dict(n.value):
            if not remove(n):  # last node can't remove itself
                prev.next = None
                n = None
        else:
            prev = n
            n = n.next
    return True


if __name__ == '__main__':
    list = Node(1)
    last = list.push(2).push(2).push(3).push(4).push(3)
    print(list)  # 1->2->2->3->4->3
    remove_dups(list)
    print(list)  # 1->2->3->4
