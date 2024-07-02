# task - 03

import numpy as np


def print_matrix(m):
    row, col = m.shape
    for i in range(row):
        c = 1
        print("|", end="")
        for j in range(col):
            c += 1
            if len(str(m[i][j])) == 1:
                print(" ", m[i][j], end="  |")
                c += 6
            else:
                print(" ", m[i][j], end=" |")
                c += 6
        print()
        print("-" * (c - col))


def reverse_Matrix(matrix):
    # TO DO

    row, col = matrix.shape

    new_matrix = np.zeros((row, col))
    nr = 0
    nc = 0

    for i in range(row - 1, -1, -1):
        nc = 0
        for j in range(col - 1, -1, -1):
            new_matrix[nr, nc] = matrix[i, j]
            nc += 1
        nr += 1

    print("Reversed Matrix:")
    return new_matrix


matrix = np.array([[14, 8, 0, 4], [9, 8, 13, 13], [9, 3, 1, 4], [2, 10, 13, 6]])


print_matrix(matrix)
reversed_matrix = reverse_Matrix(matrix)
print_matrix(reversed_matrix)

# This should print
# |  6  |  13 |  10 |  2  |
# -------------------------
# |  4  |  1  |  3  |  9  |
# -------------------------
# |  13  |  13  |  8 |  9 |
# -------------------------
# |  4 |  0  |  8  |  14  |
# -------------------------
