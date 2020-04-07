import math


def magic_index(A, offset=0, r=[]):
    if len(A) == 0:
        return r
    ind = math.floor(len(A)/2)
    if A[ind] == ind + offset:
        r.append(ind + offset)
        magic_index(A[:ind], offset, r)
        magic_index(A[ind+1:], ind + 1, r)
        return r
    if A[ind] < ind:
        magic_index(A[ind+1:], ind + 1, r)
        return r
    if A[ind] > ind:
        magic_index(A[:ind], offset, r)
        return r


if __name__ == '__main__':
    print(magic_index([-10, -3, -1, 0, 3, 5, 6, 10]))
