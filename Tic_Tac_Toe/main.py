#--Global Variables -------
#Board
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

#If game is still going
game_still_going = True
#Who won? or Tie?
winner = None
#Whos turn is it
current_player = "X"

#Display Board of Tic Tac Toe board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Play Game Function
def play_game():
    #Display initial board
    display_board()

    #WHILE LOOP for the game still going
    while game_still_going:
        #Handle a single turn of an arbitary player
        handle_turn(current_player)

        #Check if the game has ended
        check_if_game_over()

        #Flip to other player
        flip_player()

    #IF STATEMENT
    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + "won.")
    elif winner == None:
        print("Tie.")

#Handle Turn Function
def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    #Make sure the position starts at 1 instead of 0
    position = int(position) - 1

    board[position] = "X"
    display_board()

#Check if Game Over Function
def check_if_game_over():
    check_for_winner()
    check_if_tie()

#Check if Win Function
def check_for_winner():
    #Check rows
    row_winner = check_rows()

    #Check columns
    column_winner =  check_columns()

    #Check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner()
    elif column_winner:
        #there was a win
        winner = column_winner()
    elif diagonal_winner:
        winner = diagonal_winner()
    else:
        winner = None
    return

def check_rows():
    return

def check_columns():
    return

def check_diagonals():
    return

#Check if Tie Function
def check_if_tie():
    return

def flip_player():
    return

#Play Game
play_game()

