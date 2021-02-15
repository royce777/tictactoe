import random

def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def boardIsFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def checkPosition (board, x):
    return board[x] == ' '

def pickRandom(board):
    free = []
    for i in range(10):
        if board[i] == ' ' and i != 0:
            free.append(i)
    return random.choice(free)

def playerMove(board):
    ok = False
    while not(ok):
        x = int(input("Enter your X position [ 1-9 ] : "))
        if(checkPosition(board, x)):
                    board[x] = 'X'
                    ok = True

def computerMove(board):
    pos = pickRandom(board)
    board[pos] = 'O'
    print("computer put O in pos " + str(pos))

def checkWinner ( board, el):
    return ((board[7] ==el and board[8] ==el and board[9] ==el) or # across the top
    (board[4] ==el and board[5] ==el and board[6] ==el) or # across the middle
    (board[1] ==el and board[2] ==el and board[3] ==el) or # across the bottom
    (board[7] ==el and board[4] ==el and board[1] ==el) or # down the left side
    (board[8] ==el and board[5] ==el and board[2] ==el) or # down the middle
    (board[9] ==el and board[6] ==el and board[3] ==el) or # down the right side
    (board[7] ==el and board[5] ==el and board[3] ==el) or # diagonal
    (board[9] ==el and board[5] ==el and board[1] ==el)) # diagonal


def main():
    board = [' ']*10
    printBoard(board)
    while not (boardIsFull(board)):
        playerMove(board)
        if checkWinner(board, 'X'):
            print("Congratulations, You WON  !!")
            printBoard(board)
            break
        if boardIsFull(board):
            break
        computerMove(board)
        if checkWinner(board, 'O'):
            print("Sorry, you lost ! Try again !")
            printBoard(board)
            break
        printBoard(board)

    if boardIsFull(board):
        print("Tie !!!")

main()


