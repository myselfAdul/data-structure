import numpy as np


def calculate_points(matrix):
    rows, cols = matrix.shape
    total_points = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] % 50 == 0 and matrix[r][c] != 0:
                # above
                if r > 0 and matrix[r - 1][c] == 2:
                    total_points += 2
                # below
                if r < rows - 1 and matrix[r + 1][c] == 2:
                    total_points += 2
                # left
                if c > 0 and matrix[r][c - 1] == 2:
                    total_points += 2
                # right
                if c < cols - 1 and matrix[r][c + 1] == 2:
                    total_points += 2

    return total_points


def is_team_survived(matrix):
    points_gained = calculate_points(matrix)
    print(f"Points Gained: {points_gained}.", end=" ")
    if points_gained >= 10:
        print("Your team has survived the game.")
    else:
        print("Your team is out.")


# Sample Input 1
matrix = np.array([[0, 2, 2, 0], [50, 1, 2, 0], [2, 2, 2, 0], [1, 100, 2, 0]])

# matrix = np.array(
#     [[0, 2, 2, 0, 2], [1, 50, 2, 1, 100], [2, 2, 2, 0, 2], [0, 200, 2, 0, 0]]
# )

is_team_survived(matrix)
