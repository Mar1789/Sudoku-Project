import random

def remove_cells(board, cells_to_remove):
    removed = []
    for i in range(0, cells_to_remove + 1):
        c_row = int(round(random.random() * 8, 0))
        c_col = int(round(random.random() * 8, 0))
        if not [c_row, c_col] in removed:
            board[c_row][c_col] = 0
            removed.append([c_row, c_col])
        else:
            while [c_row, c_col] in removed:
                c_row = int(round(random.random() * 8, 0))
                c_col = int(round(random.random() * 8, 0))
            board[c_row][c_col] = 0
    return board
