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


def k_last(n, k):
    i = 0
    k_lasts = [0] * k
    k_lasts[i % k] = n
    while n.next:
        n = n.next
        i += 1
        k_lasts[i % k] = n
    if i > k:
        return k_lasts[(i+1) % k]
    return k_lasts[0]


if __name__ == '__main__':
    list = Node(1)
    last = list.push(2).push(2).push(3).push(4).push(3)
    print(list)
    print(k_last(list, 3))
