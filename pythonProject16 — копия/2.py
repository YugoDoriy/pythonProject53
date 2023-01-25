#Rock Paper Scissors
import random

player_choice = ''
bot_choice = ''
player_score = 0
bot_score = 0

for i in range(1, 3 + 1):
    print(f'ROUND {i}')

    player_choice = str(input('Enter choice : [r], [p], [s] : '))
    bot_choice = random.choice('rps')

    print(f'Player choice: {player_choice} Bot choice: {bot_choice}')

    if player_choice == bot_choice:
        print('Draw round')
    elif player_choice == 'r':
        if bot_choice == 's':
            print('Player WIN the round')
            player_score += 1
        elif bot_choice == 'p':
            print('Bot WIN the round')
            bot_score += 1
    elif player_choice == 's':
        if bot_choice == 'p':
            print('Player WIN the round')
            player_score += 1
        elif bot_choice == 'r':
            print('Bot WIN the round')
            bot_score += 1
    elif player_choice == 'p':
        if bot_choice == 'r':
            print('Player WIN the round')
            player_score += 1
        elif bot_choice == 's':
            print('Bot WIN the round')
            bot_score += 1

if player_score > bot_score:
    print(f'Player win the battle with score : {player_score} : {bot_score}')
elif player_score < bot_score:
    print(f'Bot win the battle with score : {bot_score} : {player_score} ')
elif player_score == bot_score:
    print(f'the score is equal : {player_score} : {bot_score} ')
else:
    print('Smathing is going wrong')








# num_1, num_2 = map(int, input('Enter two digits: ').split())
#
# if num_1 > num_2:
#     c = num_1
#     num_1 = num_2
#     num_2 = c
# summa = 0
# count = 0
# for i in range(num_1, num_2 + 1):
#     summa += i
#     count += 1
#     print(i, end = ' ')
# average = summa / count
# result = f'''\nSumma numbers = {summa}
# Average = {average}'''
# print(result)