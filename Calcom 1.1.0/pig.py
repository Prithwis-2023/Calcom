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