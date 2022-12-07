from sudoku_generator import *
from board import *
from remove_cells import *

program_running = True
sudoku_difficulty = 0

while program_running:
    if sudoku_difficulty == 0: #runs at start and when restart
        print("Difficulties: '1' for Easy, '2' for Medium, and '3' for Hard.")
        sudoku_difficulty = int(input("Choose Difficulty: "))
    elif sudoku_difficulty == -1: #runs when board is full and correct
        user_inpt = input("You WON! Type 'restart' to return to the difficulty select or 'exit' to exit the program.")
        if user_inpt == 'restart':
            difficulty = 0
        elif user_inpt == 'exit':
            program_running = False
        else:
            print("Error: Incorrect command")
    elif sudoku_difficulty == -2: #runs when board is full and incorrect
        user_inpt = input("You LOST! Type 'restart' to return to the difficulty select or 'exit' to exit the program.")
        if user_inpt == 'restart':
            difficulty = 0
        elif user_inpt == 'exit':
            program_running = False
        else:
            print("Error: Incorrect command")
    elif sudoku_difficulty == 1 or sudoku_difficulty == 2 or sudoku_difficulty == 3: #runs when difficulty is selected
        print("You can choose 'edit' to edit the board or 'reset' to reset to board.")
        print("You can also type 'restart' to return to the difficulty select or 'exit' to exit the program.")
        full_board = generate_sudoku(9, 0)
        sudoku_board = remove_cells(full_board,20+10*(sudoku_difficulty))
        sudoku_running = True
        while sudoku_running:
            print("")
            update_board(sudoku_board)
            user_inpt = input("What do you want to do? ")
            if user_inpt == 'edit':
                user_row = int(input("Enter the row from the top you want to edit. "))
                user_column = int(input("Enter the column from the left you want to edit. "))
                #####user_number = int(input("Enter the number you want to change. "))
                sudoku_board = select(sudoku_board,user_row,user_column)
            elif user_inpt == 'reset':
                sudoku_board = reset_to_original(sudoku_board)
            elif user_inpt == 'restart':
                sudoku_difficulty = 0
                sudoku_running = False
            elif user_inpt == 'exit':
                program_running = False
                sudoku_running = False
            else:
                print("Error: Incorrect command")
            if is_full(sudoku_board,0) == True:
                sudoku_running = False
                if check_board(sudoku_board,full_board) == True:
                    difficulty = -1
                else:
                    difficulty = -2
    else:
        print("Error: Incorrect sudoku_difficulty")
        print("Difficulties: '1' for Easy, '2' for Medium, and '3' for Hard.")
        sudoku_difficulty = int(input("Choose Difficulty: "))