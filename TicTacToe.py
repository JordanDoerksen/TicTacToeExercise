import copy
import os

##TESTED AND WORKING

#Clear the console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')



rows = 3  # int(input("How many rows would you like? "))
cols = 3  # int(input("How many cols would you like? "))
board = [[0 for i in range(cols)] for j in range(rows)]
# board[row,col]

x = 1
o = 2
gamePiece = {1: "X", 2: "O"}





# returns 0 if no winner
# returns 1 if x wins
# returns 2 if o wins
# returns 4 if tie
def getWinner(board):
    global rows
    global cols
    # check for tie
    isTie = True
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                isTie = False
                break
    if isTie:
        return 4
    # for each row in the board
    for i in range(rows):
        # if all the values are the same and not zero
        if board[i][0] != 0 and board[i][:-1] == board[i][1:]:
            # return winner
            return board[i][0]
    # for each col in the board
    for i in range(cols):
        # create a temp list with only items in that column
        tempCol = [board[y][i] for y in range(rows)]
        # if all the values are the same and not zero
        if tempCol[i] != 0 and tempCol[:-1] == tempCol[1:]:
            return tempCol[i]
    # diagonal wins only work on squere boards
    if cols == rows:
        # top left to bottom right
        tempDiag = [board[i][i] for i in range(rows)]
        if tempDiag[0] != 0 and tempDiag[:-1] == tempDiag[1:]:
            return tempDiag[0]
        # top right to bottom left
        tempDiag = [board[i][rows - 1 - i] for i in range(rows)]
        if tempDiag[0] != 0 and tempDiag[:-1] == tempDiag[1:]:
            return tempDiag[0]
    return 0


def playAllGames(currentBoard, player, tie=0, xWins=0, oWins=0):
    tempWinner = getWinner(currentBoard)
    otherPlayer = x if player == o else o
    if tempWinner == 0:
        for row in range(rows):
            for col in range(cols):
                if currentBoard[row][col] == 0:
                    tempBoard = copy.deepcopy(currentBoard)
                    tempBoard[row][col] = player
                    tie, xWins, oWins = playAllGames(tempBoard, otherPlayer, tie, xWins, oWins)
    elif tempWinner == 1:
        return tie, xWins + 1, oWins
    elif tempWinner == 2:
        return tie, xWins, oWins + 1
    elif tempWinner == 4:
        return tie + 1, xWins, oWins
    return tie, xWins, oWins

def print_board(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            print(value if value != 0 else ((i*3) + (j+1)), end='')
            print("|" if j < cols - 1 else "\n", end='')
        print('—'*(cols*2-1))

def player_goes(board, player):
    print_board(board)
    print(f"Your turn place your {gamePiece[player]}")
    validMove = False
    move = None
    moveRow = None
    moveCol = None
    while not validMove:
        move = int(input("Where would you like to play? "))
        moveRow = (move - 1) // 3
        moveCol = (move - 1) % 3
        if(board[moveRow][moveCol] == 0):
            validMove = True
        else:
            cls()
            print_board(board)
            print("You cannot play there?")
    board[moveRow][moveCol] = gamePiece[player]
    return board


#########WORKING ON



def computer_goes(board, player):
    print(f"Computer is playing {gamePiece[player]}")
    return board

def play_pvp_game(board):
    cls()
    print("You will now play a game against another person")


def play_pvc_game(board):
    cls()
    print("You will now play against a computer. Good Luck...")
    print("Would you like to play as x or o? x goes first\nx : 1\no : 2")
    player = int(input("Selection: "))
    computer = x if player == 2 else o
    cls()
    print(f"You have chosen to play as {gamePiece[player]} you go {'first' if player == 1 else 'last'}")
    turn = 0
    while getWinner(board) == 0:
        if (turn % 2 == 0 and player == 1) or (turn % 2 == 1 and player == 2):
            board = player_goes(board, player)
            turn += 1
        else:
            board = computer_goes(board, computer)
            turn += 1



cls()
# 0 = PvC
# 1 = PvP
gameMode = 0  # int(input("Would you like to play against a computer or another human?\n0 : vs. Computer\n1 : vs.
# User\nSelection: "))

if gameMode:
    play_pvp_game(board)
else:
    play_pvc_game(board)
