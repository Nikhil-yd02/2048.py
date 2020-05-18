def main():

    import numpy as np
    import random as ran
    import os

    # Checking given Win Number Input validity(i.e. win_num == 2**some_number):
    def pow_of_2(win_num, r,  temp_win_num):
        if r == 0:
            temp_win_num = win_num

        if win_num != 1:
            rem = win_num % 2
            if rem == 0:
                win_num //= 2
                r += 1
                return pow_of_2(win_num, r, temp_win_num)
            else:
                print('\nINVALID INPUT TAKING DEFAULT VALUE!')
                return 2048
        else:
            return temp_win_num

    # Displaying game_board:
    def display(game_board):
        if os.name == 'posix':
            # for mac/linux:
            os.system('clear')
        else:
            # for Windows:
            os.system('cls')
        print(game_board)
        return

    # Losing condition:
    def game_over(game_board):
        temp_board1 = np.copy(game_board)
        temp_board2 = np.copy(game_board)
        temp_board1 = up_merge(temp_board1)
        if (temp_board1 == temp_board2).all():
            temp_board1 = down_merge(temp_board1)
            if (temp_board1 == temp_board2).all():
                temp_board1 = left_merge(temp_board1)
                if (temp_board1 == temp_board2).all():
                    temp_board1 = right_merge(temp_board1)
                    if (temp_board1 == temp_board2).all():
                        return True

        return False

    # Defining transpose function:
    def transpose(game_board):
        for i in range(board_size):
            for j in range(i, board_size):
                if i != j:
                    game_board[i][j], game_board[j][i] = game_board[j][i], game_board[i][j]

        return game_board

    # Defining reverse function:
    def reverse(game_board):
        for row in game_board:
            for i in range(board_size//2):
                row[i], row[board_size-i-1] = row[board_size-i-1], row[i]

        return game_board

    # Performing User Input operations(up/left/down/right):
    def left_merge(game_board):
        for row in game_board:

            # Moving everything to left as much as possible:
            for j in range(board_size-1):
                for i in range(board_size-1, 0, -1):
                    if row[i-1] == 0:
                        row[i-1] = row[i]
                        row[i] = 0

            # Merging number to left
            for j in range(board_size-1):
                if row[j] == row[j+1]:
                    row[j] *= 2
                    row[j+1] = 0

            # Moving everything to left as much as possible:
            for j in range(board_size-1):
                for i in range(board_size-1, 0, -1):
                    if row[i-1] == 0:
                        row[i-1] = row[i]
                        row[i] = 0

        return game_board

    def up_merge(game_board):
        game_board = transpose(game_board)
        game_board = left_merge(game_board)
        game_board = transpose(game_board)

        return game_board

    def right_merge(game_board):
        game_board = reverse(game_board)
        game_board = left_merge(game_board)
        game_board = reverse(game_board)

        return game_board

    def down_merge(game_board):
        game_board = transpose(game_board)
        game_board = right_merge(game_board)
        game_board = transpose(game_board)

        return game_board

    # Generating '2' at random position:
    def random_2(game_board):
        if 0 in game_board:
            j = ran.randint(0, board_size - 1)
            i = ran.randint(0, board_size - 1)
            if game_board[i][j] == 0:
                game_board[i][j] = 2
                return
            else:
                random_2(game_board)

    # Creating Game Board:

    # Board Size Input:
    try:
        board_size = int(input('\nEnter size of Game_board[Default:5]: ') or '5')
        if board_size <= 0:
            print('\nINVALID INPUT TAKING DEFAULT VALUE!\n')
            board_size = 5
    except:
        print('\nINVALID INPUT TAKING DEFAULT VALUE!\n')
        board_size = 5

    # Win Number Input:
    try:
        win_num = int(input('Enter Wining_Number[Default:2048]: ') or '2048')
    except:
        print('\nINVALID INPUT TAKING DEFAULT VALUE!')
        win_num = 2048

    if win_num <= 1:
        print('\nINVALID INPUT TAKING DEFAULT VALUE!')
        win_num = 2048
    else:
        # Checking for pow of 2:
        r, temp_win_num = 0, 0
        win_num = pow_of_2(win_num, r, temp_win_num)

    start_game = input('\n||WELCOME TO 2048||\nPress ENTER to Play!')
    game_board = np.zeros((board_size, board_size), int)
    random_2(game_board)
    display(game_board)

    # User Input and Win or Lost:
    while win_num not in game_board:
        m = input('MAKE YOUR MOVE! (W/A/S/D): ')
        if m == 'W' or m == 'w':
            game_board = up_merge(game_board)
            random_2(game_board)
            display(game_board)
        elif m == 'A' or m == 'a':
            game_board = left_merge(game_board)
            random_2(game_board)
            display(game_board)
        elif m == 'S' or m == 's':
            game_board = down_merge(game_board)
            random_2(game_board)
            display(game_board)
        elif m == 'D' or m == 'd':
            game_board = right_merge(game_board)
            random_2(game_board)
            display(game_board)
        else:
            display(game_board)
            print('\nINVALID INPUT!!\nTRY AGAIN WITH (W/A/S/D)\n')

        if 0 not in game_board:
            if game_over(game_board):
                print('\nBETTER LUCK NEXT TIME!!\n||GAME OVER||')
                break
    else:
        print('\nCONGRATULATIONS!!\n||YOU WON||')

    # Restart Game:
    restart = input('\nWANT TO PLAY AGAIN?? (Y/N): ')
    if restart == 'Y' or restart == 'y':
        if os.name == 'posix':
            # for mac/linux:
            os.system('clear')
        else:
            # for Windows:
            os.system('cls')
        main()


main()
