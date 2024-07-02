# task - 1

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


def walk_zigzag(floor):
    # TO DO
    row, col = floor.shape
    flag = True

    for i in range(col):
        if flag:
            for j in range(row):
                if j % 2 == 0:  # Even index values
                    print(floor[j, i], end = " ")
        else:
            for j in range(row-1, -1, -1):
                if j % 2 != 0:  # Odd index values
                    print(floor[j, i], end = " ")
        print("\n")
        flag = not flag


floor = np.array(
    [
        ["3", "8", "4", "6", "1"],
        ["7", "2", "1", "9", "3"],
        ["9", "0", "7", "5", "8"],
        ["2", "1", "3", "4", "0"],
        ["1", "4", "2", "8", "6"],
    ]
)

print_matrix(floor)
print("Walking Sequence:")
walk_zigzag(floor)
# This should print
# 3 9 1
# 1 2
# 4 7 2
# 4 9
# 1 8 6
