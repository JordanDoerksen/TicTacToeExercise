import copy
##TESTED AND WORKING
rows = 3  # int(input("How many rows would you like? "))
cols = 3  # int(input("How many cols would you like? "))
board = [[0 for i in range(cols)] for j in range(rows)]

x = 1
o = 2


# board[row,col]


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


# print board
for row in board:
    print(row)


#########WORKING ON RECURSIVLY PLAYING ALL GAMES TO FIND BEST NEXT MOVE


def playAllGames(currentBoard, player, tie=0, xWins=0, oWins=0):
    tempWinner = getWinner(currentBoard)
    otherPlayer = x if player == o else o
    if tempWinner == 0:
        for row in range(rows):
            for col in range(cols):
                if currentBoard[row][col] == 0:
                    tempBoard = copy.deepcopy(currentBoard)
                    tempBoard[row][col] = player
                    tie, xWins, oWins = playAllGames(tempBoard,otherPlayer,tie,xWins,oWins)
    elif tempWinner == 1:
        return tie, xWins + 1, oWins
    elif tempWinner == 2:
        return tie, xWins, oWins + 1
    elif tempWinner == 4:
        return tie + 1, xWins, oWins
    return tie,xWins,oWins




print(playAllGames(board,x))
for row in board:
    print(row)
# board2 = copy.deepcopy(board)
# board2[0][0] = 2
# for row in board:
#     print(row)
# for row in board2:
#     print(row)
# returns tie,xWins,oWins
# def playAllGames(currentBoard, player, tie=0, xWins=0, oWins=0):
#     otherPlayer = x if player == o else o
#     for row in range(rows):
#         for col in range(cols):
#             if currentBoard[row][col] == 0:
#                 currentBoard[row][col] = player
#                 tempWinner = getWinner(currentBoard)
#                 if tempWinner == 0:
#                     print("test")
#                     tie, xWins, oWins = playAllGames(currentBoard, otherPlayer, tie, xWins, oWins)
#                 elif tempWinner == 1:
#                     tie, xWins + 1, oWins
#                 elif tempWinner == 2:
#                     tie, xWins, oWins + 1
#                 elif tempWinner == 4:
#                     tie + 1, xWins, oWins
#     return tie, xWins, oWins
