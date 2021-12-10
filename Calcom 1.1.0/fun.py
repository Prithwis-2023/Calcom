
print("Welcome to the Calcom Fun-Zone. We have the following features:")
def fun():
  print("*********************************************\nDrawing\n=============================================\nPig (Dice Game)\n=============================================\nPlay Connect4\n=============================================")
  f_list = ["Drawing", "Pig (Dice Game)", "Play Connect4"]
  option = input("Enter the option of your choice: ")
  while (option not in f_list):
    print("Wrong Input! Please try again.")
    option = input("Enter the option of your choice: ")
  if option == "Drawing": 
    import turtle
    from turtle import color, begin_fill, pendown, forward, right, end_fill
    print('This part can draw polygons. Describe your shape...')
    sides = int(input('Enter the number of sides: '))
    size = int(input('Size of shape (Number from 10 - 125 for best results): '))
    colour = input('Color of Shape: ')
    def polygon(sides, size, colour):
        pendown()
        color('black', colour)
        begin_fill()
        for i in range(sides):
            forward(size)
            right(360-((sides-2 * 180)/sides)+ 1)
        end_fill()
    polygon(sides, size, colour)

  elif option == "Play Connect4":
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

  elif option == "Pig (Dice Game)":
    print("""
    _____________________
   /                    /|
  /                    / |     |_____________   _______________      _____________
 /                    /  |     | |          |  |       |       |     |            |
/___________________ /   |       |          |          |             |               
|                   |    |       |          |          |             | 
|                   |    |       |__________|          |             |           ___           
|                   |    /       |                     |             |            |       
|                   |   /        |                     |             |            |      
|                   |  /         |                     |             |            | 
|                   | /       |__|___|         |_______|_______|     |____________|
|___________________|/ 
  
  
  """)
    import random
    score_p1, score_p2 = 0, 0
    winnum = int(input("Enter the winning number: "))
    while (winnum < 2):
      print("Should be greater than 2. Please try again!")
      winnum = int(input("Enter the winning number: "))
    print(f'This is the dice game called "Pig"\nThe number you roll is added to your score, and you can keep rolling as long as you like, \nbut if you roll a 1 then 0 pts are added to your score. \nFirst to {winnum} wins!')
    player1 = input('Name of player 1: ')
    player2 = input('Name of player 2: ')
    turn = 1

    def play(player, n, score_p1, score_p2):
        num_list = [0]
        move = -1
        while move != 'hold':
            move = input('roll or hold?: ')
            if move == 'roll':
                num = random.randint(1, 6)
                print(f'You have rolled a {num}')
                num_list.append(num)
                if n == 1:
                    score_p1 += num
                elif n == 2:
                    score_p2 += num
                if num == 1:
                    print('Oh... bad luck! you rolled a 1')
                    if n == 1:
                        score_p1 -= sum(num_list)
                    elif n == 2:
                        score_p2 -= sum(num_list)
                    pts = 0
                    break
            if move == 'hold':
                pts = sum(num_list)
                print(f'Nice, you earned {pts} points!')
            if n == 1:
                if score_p1 >= winnum:
                    print("=============================================")
                    print('Hurray! You win :)')
                    return score_p1, score_p2
                    break
            if n == 2:
                if score_p2 >= winnum:
                    print("=============================================")
                    print('Hurray! You win :)')
                    return score_p1, score_p2
                    break
        return score_p1, score_p2

    while max(score_p1, score_p2) < winnum:
        if turn == 1:
            print('Now it\'s player 1\'s turn!')
            score_p1, score_p2 = play(player1, 1, score_p1, score_p2)
            turn = 2
        elif turn == 2:
            print('Now it\'s player 2\'s turn!')
            score_p1, score_p2 = play(player2, 2, score_p1, score_p2)
            turn = 1
        current_score = f'\n    {player1}\'s score: {score_p1}\n    {player2}\'s score: {score_p2}\n'
        print(current_score)
    
while True:
  fun()
  contin = ""
  if contin not in ["no", "n", "yes", "y"]:
    contin = input(f"Do you wish to use again? (Yes/No): ")
    wish = ["Yes", "No"]
    while (contin not in wish):
          print("Wrong Input! Please try again.")
          contin = input(f"Do you wish to enter another calculation? (Yes/No): ")
    if contin.lower() in ["no", "n"]:
      break
    elif contin.lower() in ["yes", "y"]:
      continue

