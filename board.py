select_count = 0
original_board = None
cur_board = None

def clear(board):
    pass


def select(board, row, col):
    global select_count
    global original_board
    global cur_board
    if select_count == 0:
        original_board = board
    for index_rows, rows, in enumerate(board):
        for index_cols, cols in enumerate(rows):
            if index_rows+1 == row and index_cols+1 == col:
                #option = input("Would you like to edit the value or sketch?")
                #if option == 'edit':
                value = input("Please entered the desired value. ")
                place_number(value, board, row-1, col-1)
                select_count += 1
                return cur_board


def place_number(value, board, row, col):
    board[row][col] = int(value)
    global cur_board
    cur_board = board


def update_board(sudoku_board):
    index_row = 0
    for row in sudoku_board: #print board with single digit and spaced out by box
        for index_column in range(0,len(row)):
            print(f"{row[index_column]}", end=" ")
            if (index_column+1)%3 == 0 and index_column != 0: #third number double space
                print(end=" ")
        print("")
        if (index_row+1)%3 == 0 and index_row != 0: #third column space
            print("")
        index_row += 1


def is_full(board, empty):
    count = 0
    for row in board:
        for col in row:
            if col != empty:
                count += 1
    if count == len(board) * len(board[0]):
        return True
    else:
        return False


def check_board(board,correct_board):
    global select_count
    select_count = 0
    if board == correct_board:
        return True
    else:
        return False

def reset_to_original(sudoku_board):
    global cur_board
    global original_board
    global select_count
    if select_count == 0:
        original_board = sudoku_board
    cur_board = original_board
    select_count = 0
    return cur_board
