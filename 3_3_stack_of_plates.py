import math


class Stack:
    def __init__(self):
        self.max_n = 5
        self.arrays = {}
        self.arrays[0] = [0] * self.max_n
        self.index = -1

    def push(self, v):
        self.index += 1
        row = math.floor(self.index / self.max_n)
        offset = self.index % self.max_n
        if row not in self.arrays:
            self.arrays[row] = [0] * self.max_n
        self.arrays[row][offset] = v
        return self

    def pop(self):
        row = math.floor(self.index / self.max_n)
        offset = self.index % self.max_n
        return_value = self.arrays[row][offset]
        self.arrays[row][offset] = None
        while self.index > -1 and (self.arrays[row][offset] is None):
            self.index -= 1
            row = math.floor(self.index / self.max_n)
            offset = self.index % self.max_n
        return return_value

    def remove_at(self, k):
        if(k > self.index):
            return False
        if(k == self.index):
            self.pop()
            return self
        row = math.floor(k / self.max_n)
        offset = k % self.max_n
        self.arrays[row][offset] = None
        return self


if __name__ == '__main__':
    s = Stack()
    for i in range(10):
        s.push(i)
    s.remove_at(4)
    s.remove_at(8)
    print(s.pop())  # 9
    print(s.pop())  # 7
    print(s.pop())  # 6
    print(s.pop())  # 5
    print(s.pop())  # 3
    print(s.pop())  # 2
    print(s.pop())  # 1
    print(s.arrays)  # {0: [0, 1, 2, 3, None], 1: [5, 6, 7, None, 9]}
