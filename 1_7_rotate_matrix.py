import numpy as np
import math

def rotate_matrix(A):
    n = math.floor(len(A) / 2)
    for L in range(n):  # level
        m = len(A) - 1 - L
        for j in range(m):
            A[L][L+j], A[m-L-j][L]   = A[m-L-j][L],   A[L][L+j]
            A[L][L+j], A[m-L][m-L-j] = A[m-L][m-L-j], A[L][L+j]
            A[L][L+j], A[L+j][m-L]   = A[L+j][m-L],   A[L][L+j]
            print(np.array(A),L,j)
    return A

if __name__ == '__main__':
    A = np.array(range(1,17)).reshape(4, 4)
    print(A)
    print(np.array(rotate_matrix(A)))
