# task 2

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


def row_rotation(exam_week, seat_status):
    # To Do
    row, col = seat_status.shape

    for i in range(exam_week - 1):
        lst_item = list(seat_status[-1])
        lst_index = len(seat_status) - 1

        for i in range(lst_index, 0, -1):
            seat_status[i] = seat_status[i - 1]
        
        # Convert back to numpy array and place the last row in the first position
        seat_status[0] = np.array(lst_item)
        

    print("Updated seat status:")
    print(seat_status)

    # Find the row of "AA" final
    for i in range(row):
        if "AA" in seat_status[i]:
            return i + 1  


seat_status = np.array(
    [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        ["P", "Q", "R", "S", "T"],
        ["U", "V", "W", "X", "Y"],
        ["Z", "AA", "BB", "CC", "DD"],
    ]
)

exam_week = 3
print_matrix(seat_status)
print()
row_number = row_rotation(exam_week, seat_status)
# This should print modified seat status after rotation
print(f"Your friend AA will be on row {row_number}")
# This should print Your friend AA will be on row 2
