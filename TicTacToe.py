# Background info

# This is a Tic-Tac-Toe game made in Python by MadaraCodes
# 11 Oct 2022
# ------------------------------------------

# Objectives

# print game board
# take player input
# check for win or tie
# create basic AI that uses the random module to make decisions
# switch turns between player and AI
# ----------------------------------

import random # adding random module to use for AI

# formatting board

board = ["-", "-", "-",
        "-", "-", "-", 
        "-", "-", "-"]

# defining variables
currentPlayer = "X"
winner = None
gameRunning = True

#printing game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input
def playerInput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer # lists start with 0 so you subtract 1 for the placeholders to be targeted
    else:
        print("That spot is occupied!")
        switchPlayer()
        

# check win or tie
# global keyword (for functions) changes variable to entire file if it changes during the game
# this checks horizontal win
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# this checks verticle row win
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# this checks diagonal win
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# checks for tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        printBoard(board)
        gameRunning = False

# checks for win
# f string types strings faster than adding stuff together
def checkWin():
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")
        printBoard(board)
        gameRunning = False

# switch turns to AI
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"

# create basic AI with random module
def AI(board):
    while currentPlayer == "0":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()

# game loop
while gameRunning:
    printBoard(board)

    playerInput(board)
    checkWin()
    checkTie(board)

    switchPlayer()

    AI(board)
    checkWin()
    checkTie(board)
