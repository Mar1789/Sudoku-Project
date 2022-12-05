def clear(board):
    pass

def select(board, row, col):
    for index_rows, rows in enumerate(board):
        for index_cols, cols in enumerate(rows):
            if index_rows == row and index_cols == col:
                option = input("Would you like to edit the value or sketch?")
                if option == 'edit':
                    value = input("Please entered the desired value.")
                    place_number(value, board, row, col)

def place_number(value, board, row, col):
    board[row][col] = int(value)

def reset_to_original():
    pass

def is_full(board,empty):
    count = 0
    for row in board:
        for col in row:
            if col != empty:
                count += 1
    if count == len(board)*len(board[0]):
        return True
    else:
        return False

def update_board():
    pass

def sketch():
    pass

def check_board(board):
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test = []
    count = 0
    temp = 0
    cols = 0
    for row in board:
        for i in range(0, len(row)):
            test.append(board[i][cols])
        for number in test:
            if number in number_list:
                temp += 1
        if temp == 9:
            count += 1
        test = []
        cols += 1
        temp = 0
    if count == 9:
        return True
    else:
        return False