from sudoku_generator import *

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
    else: #runs when difficulty is selected
        print("You can choose 'edit' to edit the board or 'reset' to reset to board.")
        print("You can also type 'restart' to return to the difficulty select or 'exit' to exit the program.")
        full_board = generate_sudoku(9, 0)
        #sudoku_board = (function)
        sudoku_running = True
        while sudoku_running:
            index_row = 0
            for row in sudoku_board: #print board with single digit and spaced out by box
                for index_column in range(0,len(row)):
                    print(f"{row[index_column]}", end=" ")
                    if (index_column+1)%3 == 0 and index_column != 0: #third number double space
                        print(end=" ")
                print("")
                if (index_row+1)%3 == 0 and index_row != 0: #third column space
                    print("")
            user_inpt = input("What do you want to do? ")
            if user_inpt == 'edit':
                user_row = int(input("Enter the row from the top you want to edit. "))
                user_column = int(input("Enter the column from the left you want to edit. "))
                #####user_number = int(input("Enter the number you want to change. "))
                
                #change board stuff
                
            elif user_inpt == 'reset':
                pass #reset to original
            elif user_inpt == 'restart':
                sudoku_difficulty = 0
            elif user_inpt == 'exit':
                program_running = False
                sudoku_running = False
            else:
                print("Error: Incorrect command")

            #board testing