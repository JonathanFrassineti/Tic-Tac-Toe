from random import randrange


def display_board(board):
    # Display the current board status.
    for i in range(len(board)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ", board[i][0], " ", "|  ", board[i][1], " ", "|  ", board[i][2], "  |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.
    counter = 0
    while True:
        move = int(input("Enter your move, from 1 to 9: "))
        if (move < 1 or move > 9):
            print("From 1 to 9, please.")
            continue
        if move <= 3:
            if (board[0][move - 1] != 'X' and board[0][move - 1] != 'O'):
                board[0][move - 1] = 'O'
                counter += 1
            else:
                print("Invalid position, please give me a right one.")
                continue
        elif (move > 3 and move <= 6):
            if (board[1][move - 4] != 'X' and board[1][move - 4] != 'O'):
                board[1][move - 4] = 'O'
                counter += 1
            else:
                print("Invalid position, please give me a right one.")
                continue
        else:
            if (board[2][move - 7] != 'X' and board[2][move - 7] != 'O'):
                board[2][move - 7] = 'O'
                counter += 1
            else:
                print("Invalid position, please give me a right one.")
                continue

        if counter:
            return board
        else:
            continue


def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    counter = 0
    parity = 0
    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign):
        counter = 1
    elif (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign):
        counter = 1
    elif (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign):
        counter = 1

    elif (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign):
        counter = 1
    elif (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign):
        counter = 1
    elif (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign):
        counter = 1

    elif (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign):
        counter = 1
    elif (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        counter = 1
    else:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == 'X' or board[i][j] == 'O'):
                    parity += 1
                else:
                    parity += 0
        if (parity == 9):
            counter = 2
        else:
            counter = 0

    return counter


def draw_move(board):
    # The function draws the computer's move and updates the board.
    counter = 0
    while True:
        cmove = randrange(9)
        cmove += 1
        if cmove <= 3:
            if (board[0][cmove - 1] != 'X' and board[0][cmove - 1] != 'O'):
                board[0][cmove - 1] = 'X'
                counter = 1
            else:
                continue
        elif (cmove > 3 and cmove <= 6):
            if (board[1][cmove - 4] != 'X' and board[1][cmove - 4] != 'O'):
                board[1][cmove - 4] = 'X'
                counter = 1
            else:
                continue
        else:
            if (board[2][cmove - 7] != 'X' and board[2][cmove - 7] != 'O'):
                board[2][cmove - 7] = 'X'
                counter = 1
            else:
                continue

        if counter:
            return board
        else:
            continue


# Initial board.
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
display_board(board)
while True:
    move = enter_move(board)
    display_board(move)
    user = victory_for(board, 'O')
    comp = victory_for(board, 'X')
    if (user or comp):
        if (user == 1):
            print("You won :)")
        elif (comp == 1):
            print("Computer won :(")
        else:
            print("It's a tie.")
        break
    movec = draw_move(board)
    display_board(movec)
    user = victory_for(board, 'O')
    comp = victory_for(board, 'X')
    if (user or comp):
        if (user == 1):
            print("You won :)")
        elif (comp == 1):
            print("Computer won :(")
        else:
            print("It's a tie.")
        break
