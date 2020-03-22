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

    def unshift(self, value):
        new_node = Node(self.value)
        new_node.next = self.next
        self.value = value
        self.next = new_node

    def remove(self):
        if(not self.next):
            return False
        self.value = self.next.value
        self.next = self.next.next
        return True


def partition(n, x):
    head = n
    higher = None
    while n:
        print(n)
        if(n.value >= x):
            if not higher:
                higher = Node(n.value)
            else:
                higher.unshift(n.value)
            if not n.remove():
                n.next = higher
                n.remove()
                break
        else:
            if not n.next:
                n.next = higher
                break
            n = n.next
    return head


if __name__ == '__main__':
    list = Node(1)
    last = list.push(2).push(20).push(3).push(4).push(3).push(10).push(5).push(3).push(6)
    print(list)
    print(partition(list, 5))
