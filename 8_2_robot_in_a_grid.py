import numpy as np


def search_path(board, r=0, c=0, path=[]):
    d = len(board) + len(board[0]) - r - c - 2
    if board[r][c]:
        return d + 1
    if d == 0:
        path.append([r, c])
        return 0
    if r+1 < len(board):
        if search_path(board, r+1, c, path) == 0:
            path.append([r, c])
            return 0 if r+c != 0 else path
    if c+1 < len(board[0]):
        if search_path(board, r, c+1, path) == 0:
            path.append([r, c])
            return 0 if r+c != 0 else path
    return d


def init_mem(board):
    return np.zeros([len(board), len(board[0])]).tolist()


def search_path_mem(board, r=0, c=0, path=[], mem=None):
    if mem is None:
        mem = init_mem(board)
    d = len(board) + len(board[0]) - r - c - 2
    if board[r][c]:
        return d + 1
    if d == 0:
        path.append([r, c])
        return 0
    if r+1 < len(board) and mem[r+1][c] == 0:
        if search_path_mem(board, r+1, c, path, mem) == 0:
            path.append([r, c])
            return 0 if r+c != 0 else path
    if c+1 < len(board[0]) and mem[r][c+1] == 0:
        if search_path_mem(board, r, c+1, path, mem) == 0:
            path.append([r, c])
            return 0 if r+c != 0 else path
    mem[r][c] = d
    return d


if __name__ == '__main__':
    r = 10
    c = 20
    board = np.zeros([r, c])
    board[1:, c-2] = 1
    print(board)
    print(search_path_mem(board.tolist()))
