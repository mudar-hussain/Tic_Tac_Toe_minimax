#    -*- coding: UTF-8  -*-
"""
Developer: Mudar Hussain
"""

print()
print('\t\tWelcome to Tic Tac Toe!')
print()
print('-------------------------------------------------------------------------------')
print()

game_on = True
ch = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_dict = {1: [3, 1], 2: [3, 2], 3: [3, 3], 4: [2, 1], 5: [2, 2], 6: [2, 3], 7: [1, 1], 8: [1, 2], 9: [1, 3]}


def display(row):
    print()
    print(' ' + row[0][0] + ' | ' + row[0][1] + ' | ' + row[0][2])
    print('-----------')
    print(' ' + row[1][0] + ' | ' + row[1][1] + ' | ' + row[1][2])
    print('-----------')
    print(' ' + row[2][0] + ' | ' + row[2][1] + ' | ' + row[2][2])
    print()


while game_on:
    p1 = input("Player 1 Please pick a marker 'X' or 'O' :  ").upper()
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
    row = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    print('Enter your choices according to the numpad keys as shown below: (1-9):  ')
    display(row)
    row = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


    def game_on_choice():
        global game_on
        goc = False
        while goc not in ['Y', 'N']:
            goc = input("Do you want to play again? Enter Y or N: ").upper()
            if goc not in ['Y', 'N']:
                print("Sorry I don't understand. Please enter Y or N: ")
        if goc == 'Y':
            game_on = True
            print()
        else:
            game_on = False
            print()
            print('Thank you for playing!')
            print()

    def choice(p):
        global p1, p2, ch
        num = 0
        loop = True
        while (num not in ch) or loop:
            loop = False
            r = 0
            c = 0
            num = input(f'Player {p}, Please enter no (1-9):  ')
            try:
                num = int(num)
                r, c = num_dict.get(num)
            except ValueError:
                num = 0
                loop = True
                continue
            if num not in ch:
                print('Enter numbers within range (1-3)')
                loop = True
            elif num in ch and row[r - 1][c - 1] != ' ':
                print('This position is already taken')
                loop = True
        if p == 1:
            row[r - 1][c - 1] = p1
        else:
            row[r - 1][c - 1] = p2

    def check_winner():
        if ' ' not in (row[0][0], row[1][0], row[2][0]) and row[0][0] == row[1][0] == row[2][0]: return row[0][0]
        elif ' ' not in (row[0][1], row[1][1], row[2][1]) and row[0][1] == row[1][1] == row[2][1]: return row[0][1]
        elif ' ' not in (row[0][2], row[1][2], row[2][2]) and row[0][2] == row[1][2] == row[2][2]: return row[0][2]
        elif ' ' not in (row[1][0], row[1][1], row[1][2]) and row[1][0] == row[1][1] == row[1][2]: return row[1][0]
        elif ' ' not in (row[2][0], row[2][1], row[2][2]) and row[2][0] == row[2][1] == row[2][2]: return row[2][0]
        elif ' ' not in (row[0][0], row[1][1], row[2][2]) and row[0][0] == row[1][1] == row[2][2]: return row[0][0]
        elif ' ' not in (row[0][2], row[1][1], row[2][0]) and row[0][2] == row[1][1] == row[2][0]: return row[0][2]
        return False

    print('Let\'s begin the game')
    display(row)
    i = 1
    while True:
        choice(i)
        display(row)
        winner = check_winner()
        if winner != False:
            if winner == 'X':
                if p1 == 'X': print('Player 1 wins.')
                else: print('Player 2 wins.')
            else:
                if p1 == 'O': print('Player 1 wins.')
                else: print('Player 2 wins.')
            print()
            game_on_choice()
            break
        if ' ' not in row[0] and ' ' not in row[1] and ' ' not in row[2]:
            print("It's a Tie between you two ")
            game_on_choice()
            break
        if i == 1:
            i += 1
        else:
            i -= 1