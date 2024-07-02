# task - 05

import numpy as np


def compress_matrix(mat):
    rows, cols = mat.shape
    new_rows, new_cols = rows // 2, cols // 2
    compressed_mat = np.zeros((new_rows, new_cols), dtype=int)

    for i in range(new_rows):
        for j in range(new_cols):
            compressed_mat[i, j] = (
                mat[2 * i, 2 * j]
                + mat[2 * i + 1, 2 * j]
                + mat[2 * i, 2 * j + 1]
                + mat[2 * i + 1, 2 * j + 1]
            )

    return compressed_mat


def print_matrix(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            print(f"|  {matrix[i, j]}  ", end="")
        print("|")
        print("-" * (cols * 6 + 1))


matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 3, 5, 2], [-2, 0, 6, -3]])

print("Original matrix:")
print_matrix(matrix)

returned_array = compress_matrix(matrix)

print("Compressed matrix:")
print_matrix(returned_array)
