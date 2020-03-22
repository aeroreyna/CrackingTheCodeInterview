class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        n = self
        str = "{}".format(n.value)
        count = 0
        while n.next and count < 20:
            n = n.next
            str += "->{}".format(n.value)
            count += 1
        return str

    def push(self, value):
        n = self
        while n.next:
            n = n.next
        n.next = Node(value)
        return n.next


def has_loop(n):
    """ Tells if a loop is present but not the beggining """
    fast = slow = n
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if(slow == fast):
            return True
    # No loop was founded
    return False


def loop_detection(n):
    """ Tells the beggining of a loop if existent """
    dict = {}
    dict[n] = 1
    while n.next:
        n = n.next
        if n in dict:
            return n
        dict[n] = 1
    return False


if __name__ == '__main__':
    list = Node(1)
    five = list.push(2).push(3).push(4).push(5)
    last = list.push(6).push(7)
    last.next = five
    print(list)  # 1->2->3->4->5->6->7->5->6->7->5->6->7->5->6->7->5->6->7->5->6
    loop_node = loop_detection(list)
    print(loop_node.value)  # 5
