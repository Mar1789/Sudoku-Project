import math
import random


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = int(row_length)
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(self.row_length))
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def get_board(self):
        return self.board

    def print_board(self):
        b_count = 0
        r_count = 0
        for row in self.board:
            print(f'||', end='')
            for box in row:
                print(f'| {box} ', end='')
                b_count += 1

                if b_count % 3 == 0:
                    print(f'||', end='')
            print('|\n')
            b_count = 0
            r_count += 1
            if r_count % 3 == 0:
                print()

    def valid_in_row(self, row, num):
        for numb in self.board[int(row)]:
            if numb == num:
                return False
        return True

    def valid_in_col(self, col, num):
        for i in range(0, self.row_length):
            if self.board[i][int(col)] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(int(row_start), int(row_start) + 3):
            for j in range(int(col_start), int(col_start) + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        rrow = int(row)
        ccol = int(col)

        # statements below ensure proper checking of boxes for valid_in_box
        if row in [0, 1, 2]:
            rrrow = 0
        elif row in [3, 4, 5]:
            rrrow = 3
        else:
            rrrow = 6

        if col in [0, 1, 2]:
            cccol = 0
        elif col in [3, 4, 5]:
            cccol = 3
        else:
            cccol = 6

        # nested checks of validity
        if self.valid_in_row(rrow, num):
            if self.valid_in_col(ccol, num):
                if self.valid_in_box(rrrow, cccol, num):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    # fills boxes on diagonal
    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                unused = self.unused_in_box(row_start, col_start)
                cur_rand = 0
                while cur_rand not in unused:
                    cur_rand = round(random.random() * 9, 0)
                self.board[i][j] = int(cur_rand)

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                # print(f'{row} | {col} | ({num})')
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, 3)

    def remove_cells(self):
        removed = []
        for i in range(0, self.removed_cells + 1):
            c_row = int(round(random.random() * 8, 0))
            c_col = int(round(random.random() * 8, 0))
            if not [c_row, c_col] in removed:
                self.board[c_row][c_col] = 0
                removed.append([c_row, c_col])
            else:
                while [c_row, c_col] in removed:
                    c_row = int(round(random.random() * 8, 0))
                    c_col = int(round(random.random() * 8, 0))
                self.board[c_row][c_col] = 0

    # below custom
    # function returns which numbers haven't yet been used in a box
    def unused_in_box(self, row_start, col_start):
        used_in_box = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] > 0:
                    used_in_box.append(self.board[i][j])
        for k in range(1, 10):
            if k in used_in_box:
                nums.remove(k)
        return nums

