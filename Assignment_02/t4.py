import numpy as np


# def print_matrix(m):
#     row, col = m.shape
#     for i in range(row):
#         c = 1
#         print("|", end="")
#         for j in range(col):
#             c += 1
#             if len(str(m[i][j])) == 1:
#                 print(" ", m[i][j], end="  |")
#                 c += 6
#             else:
#                 print(" ", m[i][j], end=" |")
#                 c += 6
#         print()
#         print("-" * (c - col))


def show_knight_move(knight):
    # To Do

    board = np.zeros((8, 8))

    row = knight[0] 
    col = knight[1] 
    
    # current position
    board[row, col] = 66
    
    # possible moves for knight (left,right, top, bottom)
    
    moves = [(2, 1), (2,-1), (-2,1), (-2, -1), (1,2), (-1, 2), (1, -2),(-1,-2)]
    
    for i in moves:
        nr = row + i[0]
        nc = col + i[1]
        if 0<=nr<8 and 0<=nc < 8:
            board[nr,nc] = 3   
    print(board)
    
    
    


knight = (3, 4)
chess_board = show_knight_move(knight)
# print_matrix(chess_board)


# This Should print
# | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
# ------------------------------------------
# | 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 |
# ------------------------------------------
# | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 |
# ------------------------------------------
# | 0 | 0 | 0 | 0 | 66 | 0 | 0 | 0 |
# ------------------------------------------
# | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 |
# ------------------------------------------
# | 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 |
# ------------------------------------------
# | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
# ------------------------------------------
# | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
# -----------------------------------------
