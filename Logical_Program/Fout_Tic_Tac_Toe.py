import random

ROW = 3
COLUMN = 3
EMPTY = ' '
PLAYER = 'X'
COMPUTER = 'O'

def create_board():
    """
    Description : Create 3x3 Board
    Input : None
    Output : {board : 2D Array}
    """
    board = []
    for i in range(ROW):
        row = []
        for j in range(COLUMN):
            row.append(EMPTY)
        board.append(row)
    return board

def print_board(board):
    print('\n')
    for i in range(ROW):
        for j in range(COLUMN):
            print(board[i][j], end = j == COLUMN - 1 and '\n' or ' | ')
        if i != ROW - 1:
            print(9*"-") 
        else :
            print('\n')

def is_board_full(board):
    """
    Description : check if the board is full
    Input : {board : 2D Array}
    Output : None
    """
    for i in range(ROW):
        for j in range(COLUMN):
            if board[i][j] == EMPTY:
                return False
    return True


def is_winner(board, player):
    """
    Description : check if the player has won
    Input : {board : 2D Array , player : X or 0}
    Output : {is_winnder : bool}
    """
    for i in range(ROW):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for i in range(COLUMN):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def player_move(board):
    """
    Description : Move the hance of the player
    Input : {board : 2D Array}
    Output : None
    """
    while True:
        row = int(input("Enter the row: "))
        column = int(input("Enter the column: "))
        if row < 0 or row >= ROW or column < 0 or column >= COLUMN:
            print("Invalid move. Please try again.")
        elif board[row][column] != EMPTY:
            print("Cell is already occupied. Please try again.")
        else:
            board[row][column] = PLAYER
            break


def computer_move(board):
    """
    Description : Move the hance of the computer
    Input : {board : 2D Array}
    Output : None
    """
    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if board[row][column] == EMPTY:
            board[row][column] = COMPUTER
            break


# play the game
def play_game():
    """
    Description : Run the game
    Input : None
    Output : None
    """
    board = create_board()
    print_board(board)
    while True:
        player_move(board)
        print_board(board)
        if is_winner(board, PLAYER):
            print("Player wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        computer_move(board)
        print_board(board)
        if is_winner(board, COMPUTER):
            print("Computer wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game() 


