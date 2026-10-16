from random import randrange


def display_board(board):
    # Displays the current state of the board
    print("+-------+-------+-------+")
    print(f"| | | |")
    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print(f"| | | |")
    print("+-------+-------+-------+")
    print(f"| | | |")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print(f"| | | |")
    print("+-------+-------+-------+")
    print(f"| | | |")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print(f"| | | |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move


# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.


board = [0][1][3]
display_board(board[2][0])