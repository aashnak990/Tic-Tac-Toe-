# make a board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
#if game still going (global variable)
game_still_going=True
#who won or tie
winner = None
#whos turn it is
current_player='X'

# display board
def disp_board():
    print(board[0] + '|' +board[1] + '|' +board[2])
    print(board[3] + '|' +board[4] + '|' +board[5])
    print(board[6] + '|' +board[7] + '|' +board[8])
#play game
def play_game():
    # display the initial board first
    disp_board()
    #while the game is still going
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        #flip to other flip_player
        flip_player()
    #if game has ended
    if winner == 'X' or winner =='O':
        print (winner + ' won')
    elif winner == None :
        print('Tie')
def check_if_game_over():
    check_if_winner()
    check_if_tie()
def check_if_winner():
    global winner
    #check rows
    row_winner=check_rows()
    #check coloumns
    coloumns_winner=check_coloumns()
    #check diagonals
    diagonal_winner=check_diagonal()
    if row_winner:
        winner=row_winner

    elif coloumns_winner:
        winner=coloumns_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        #no win
        winner=None
    return
def check_rows():
    global game_still_going
    row_1= board[0]==board[1]==board[2] !='-'
    row_2= board[3]==board[4]==board[5] !='-'
    row_3= board[6]==board[7]==board[8] !='-'
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_coloumns():
    global game_still_going
    col_1= board[0]==board[3]==board[6] !='-'
    col_2= board[1]==board[4]==board[7] !='-'
    col_3= board[2]==board[5]==board[8] !='-'
    if col_1 or col_2 or col_3:
       game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]

    return
def check_diagonal():
    global game_still_going
    dia_1= board[0]==board[4]==board[8] !='-'
    dia_2= board[2]==board[4]==board[6] !='-'
    if dia_1 or dia_2:
       game_still_going = False
    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
    return
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return
def flip_player():
    global current_player
    if current_player=='X':
        current_player='O'
    elif current_player=='O':
        current_player='X'
    return

def handle_turn(player):
    print(player + "'s turn")
    position=input("choose a position from 1 to 9:")
    valid=False
    while not valid:
      while position not in ['1','2','3','4','5','6','7','8','9']:
        position=input("Invalid input,choose a position from 1 to 9:")
      position=int(position) - 1
      if board[position] =='-':
        valid=True
      else:
        print("can't go there")

    board[position]=player

    disp_board()



play_game()
#display board
#play game
#handle turn
#check win
#check rows
#check coloumns
#check diagonals
#check tie
#flip player
