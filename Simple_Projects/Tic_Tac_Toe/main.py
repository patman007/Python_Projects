#--Global Variables -------
#Board
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

#If game is still going
game_still_going = True

#Who won? or Tie?
winner = None

#Whos turn is it?
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

    #While game still going
    while game_still_going:

        #Handle a single turn of an arbitary player
        handle_turn(current_player)

        #Check if the game has ended
        check_if_game_over()

        #Flip to other player
        flip_player()

    #If the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

#Handle Turn Function
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    #while the input is not valid
    valid = False
    while not valid:

        #while input is not an integer
        #Alternative could be regex here
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        #Make sure the position starts at 1 instead of 0
        position = int(position) - 1

        #if position is empty on the board
        if board[position] == "-":
            valid = True
        else:
            print('You cant go there. Go again')

    board[position] = player
    display_board()

#Check if Game Over Function
def check_if_game_over():
    check_for_winner()
    check_if_tie()

#Check if Win Function
def check_for_winner():

    #Set up Global variables
    global winner

    #Check rows
    row_winner = check_rows()

    #Check columns
    column_winner =  check_columns()

    #Check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        winner = None
    return

#Check Rows Function
def check_rows():

    #Set up global variables
    global game_still_going

    #Check if any of rows have the same value without a dash
    row_1 = board[0] == board[1] == board[2] !="-"
    row_2 = board[3] == board[4] == board[5] !="-"
    row_3 = board[6] == board[7] == board[8] !="-"

    #If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
        #Return the winner (X or O)
        #We could use any element number besides listed here
        if row_1:
            return board[0]
        elif row_2:
            return_board[3]
        elif row_3:
            return board[6]
        return

#Check Columns Function
def check_columns():

    #Set up global variables
    global game_still_going

    #Check if any of rows have the same value without a dash
    column_1 = board[0] == board[3] == board[6] !="-"
    column_2 = board[1] == board[4] == board[7] !="-"
    column_3 = board[2] == board[5] == board[8] !="-"

    #If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

        #Return the winner (X or O)
        #We could use any element number besides listed here
        if column_1:
            return board[0]
        elif column_2:
            return board[1]
        elif column_3:
            return board[2]
        return

#Check Diagonals Function
def check_diagonals():
            #Set up global variables
    global game_still_going
    #Check if any of rows have the same value without a dash
    diagonal_1 = board[0] == board[4] == board[8] !="-"
    diagonal_2 = board[6] == board[4] == board[2] !="-"

    #If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

        #Return the winner (X or O)
        #We could use any element number besides listed here
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[6]
        return

#Check if Tie Function
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

#Flip Player Function
def flip_player():
    #Global variable
    global current_player

    #If current player was X, then change it to O
    if current_player == "X":
        current_player = "O"
    elif current_player =="O":
        current_player = "X"
    return

#Play Game
play_game()

