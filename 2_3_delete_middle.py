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


def delete_middle(n):
    fast = slow = n
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # remove slow
    slow.value = slow.next.value
    slow.next = slow.next.next
    return n


if __name__ == '__main__':
    list = Node(1)
    last = list.push(2).push(3).push(4).push(5).push(6).push(7)
    delete_middle(list)
    print(list)  # 1->2->3->5->6->7
