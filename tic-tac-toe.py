#!/usr/bin/env python3

board = {
    "top-L": " ",
    "top-C": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-C": " ",
    "mid-R": " ",
    "bot-L": " ",
    "bot-C": " ",
    "bot-R": " ",
}

def print_board():
    print(board["top-L"]+"|" + board["top-C"]+"|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"]+"|" + board["mid-C"]+"|" + board["mid-R"])
    print("-+-+-")
    print(board["bot-L"]+"|" + board["bot-C"]+"|" + board["bot-R"])

def check_valid_move(move):
    valid_move = True
    if(move not in board):
        valid_move = False
    if(valid_move and board[move] != " "):
        valid_move = False
    return(valid_move)

def ask_move():
    global current_move, last_move
    current_move, last_move = last_move, current_move
    turn_over = False
    while(not turn_over):
        print(current_move.upper() + "'s move. Specify {top,mid,bot}-{L,C,R}")
        move = input()
        valid_move = check_valid_move(move)
        if(valid_move):
            board[move] = current_move
            turn_over = True
        else:
            print("Invalid move.  Choose another space.")

def check_win():
    win = False
    # check top row
    if(board['top-L'] == board['top-C'] == board['top-R'] and board['top-L'] != " "):
        win = True
    # check middle row
    if(board['mid-L'] == board['mid-C'] == board['mid-R'] and board['mid-L'] != " "):
        win = True
    # check bottom row
    if(board['bot-L'] == board['bot-C'] == board['bot-R'] and board['bot-L'] != " "):
        win = True
    # check left column
    if(board['top-L'] == board['mid-L'] == board['bot-L'] and board['top-L'] != " "):
        win = True
    # check center column
    if(board['top-C'] == board['mid-C'] == board['bot-C'] and board['top-C'] != " "):
        win = True
    # check right column
    if(board['top-R'] == board['mid-R'] == board['bot-R'] and board['top-R'] != " "):
        win = True
    # check \ diagonal
    if(board['top-L'] == board['mid-C'] == board['bot-R'] and board['top-L'] != " "):
        win = True
    # check / diagonal
    if(board['bot-L'] == board['mid-C'] == board['top-R'] and board['bot-L'] != " "):
        win = True
    return(win)

def check_over():
    full = (" " not in board.values())
    if(full):
        print("No more moves.  Stalemate.  Game over.")
    win = check_win()
    if(win):
        print("Game over.  "+current_move+" wins.")
    return(not(full) and not(win))

last_move = "x"
current_move = "o"
game_not_over = True
while(game_not_over):
    print_board()
    ask_move()
    game_not_over = check_over()
# Print board one last time
print_board()
