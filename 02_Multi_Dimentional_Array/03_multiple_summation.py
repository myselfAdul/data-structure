import numpy as np


def row_sum(m):
    rlen = len(m)
    clen = len(m[0])

    row_sum = 0

    for i in range(rlen):
        for j in range(clen):
            row_sum += m[i, j]
        print(f"Sum of row {i+1}:", row_sum)
        row_sum = 0
    pass


# row_sum(m)


def column_sum(m):
    rlen = len(m)
    clen = len(m[0])
    col_sum = 0
    for i in range(clen):
        for j in range(rlen):
            col_sum += m[j, i]
            pass
        print(f"Sum of column {i+1}:", col_sum)
        col_sum = 0
    pass


# column_sum(m)


# primary diagonal sum  \


def primary_diagonal_sum(square_matrix):
    rlen = len(square_matrix)
    clen = len(square_matrix[0])
    sum = 0
    for i in range(clen):
        sum += square_matrix[i, i]
    print(sum)


square_matrix = np.array([[4, 3, 8], [2, 5, 1], [7, 6, 9]])
# primary_diagonal_sum(square_matrix)


### secondary diagonal sum /


def secondary_diagonal_sum(s_matrix):
    sum = 0
    item = len(s_matrix) - 1
    for i in range(len(s_matrix)):
        sum += s_matrix[i, item]
        item -= 1
    print(sum)


s_matrix = np.array([[4, 3, 8, -7], [2, 5, -1, 12], [-6, 16, 9, 10], [4, 13, 11, 18]])

secondary_diagonal_sum(s_matrix)
