# connect 4 game :D

red = "X"
yellow = "O"
empty = "-"
col_num = "1 2 3 4 5 6 7"

c4_board = [
["-", "-", "-", "-", "-", "-", "-"], 
["-", "-", "-", "-", "-", "-", "-"], 
["-", "-", "-", "-", "-", "-", "-"], 
["-", "-", "-", "-", "-", "-", "-"], 
["-", "-", "-", "-", "-", "-", "-"], 
["-", "-", "-", "-", "-", "-", "-"]]

# printing c4_board to screen
def print_board(): 
    print(col_num)
    for row in c4_board:
        for checker in row:
            print(checker, end = " ")
        print()

player1 = input("Name of player one (X): ")
player2 = input("Name of player two (O): ")

print_board()

turn = 0
while True:
    if turn % 2 == 0:
        print(f"{player1}'s turn")
        person = player1
        symbol = red
    else:
        print(f"{player2}'s turn")
        person = player2
        symbol = yellow

    # check if column number is valid:
    while True:
        col = input("Column number (between 1 and 7): ")
        col = str(col)
        if col.isdigit() == True:
            col = int(col)
            rcol = col - 1
            if col >= 1 and col <= 7:
                if c4_board[0][rcol] == empty:
                    break
        print_board()
        print("Invalid input")
    rrow = 5
    while c4_board[rrow][rcol] != empty:
        rrow -= 1

    c4_board[rrow][rcol] = symbol
    print_board()

    win_mess = False
    # check row
    for i in range(4):
        if c4_board[rrow][i] == c4_board[rrow][i + 1] == c4_board[rrow][i + 2] == c4_board[rrow][i + 3] == symbol:
            win_mess = True
    # check column
    for i in range(3):
        if c4_board[i][rcol] == c4_board[i + 1][rcol] == c4_board[i + 2][rcol] == c4_board[i + 3][rcol] == symbol:
            win_mess = True
    # check diagonal slant forward
    drow = rrow - min(rrow, rcol)
    dcol = rcol - min(rrow, rcol)
    if max(drow, dcol) == drow and drow <= 3:
        times = 3 - drow
    elif max(drow, dcol) == dcol and dcol <= 4:
        times = 4 - dcol
    else:
        times = 0
    for i in range(times):
        if c4_board[drow + i][dcol + i] == c4_board[drow + 1 + i][dcol + 1 + i] == c4_board[drow + 2 + i][dcol + 2 + i] == c4_board[drow + 3 + i][dcol + 3 + i] == symbol:
            win_mess = True
    # check diagonal slant backward
    if rrow + rcol > 6:
        drow = rrow + rcol - 6
        dcol = 6
    else:
        drow = 0
        dcol = rrow + rcol
    i = 0
    while drow + 3 + i <= 5 and dcol - 3 - i >= 0:
        if c4_board[drow + i][dcol - i] == c4_board[drow + 1 + i][dcol - 1 - i] == c4_board[drow + 2 + i][dcol - 2 - i] == c4_board[drow + 3 + i][dcol - 3 - i] == symbol:
            win_mess = True
        i += 1
    if win_mess == True:
        print(f"Congratulations {person}!! You are the winner! gg")
        break
    turn += 1