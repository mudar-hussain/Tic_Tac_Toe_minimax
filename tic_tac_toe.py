p1 = input("Player 1 Please pick a marker 'X' or 'O'")
if p1 == 'X':
    p2 = 'O'
else:
    p2 = 'X'
row = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def display():
    print(row[0])
    print(row[1])
    print(row[2])


def choice(p):
    global p1, p2
    c = 0
    r = 0
    loop=True
    while (c < 1 or c > 3 or r < 1 or r > 3) or loop:
        loop = False
        c = input(f'Player {p}, Please enter column no (1-3)')
        r = input(f'Player {p}, Please enter row no (1-3)')
        try:
            c = int(c)
            r = int(r)
        except ValueError:
            c = 0
            r = 0
            loop = True
            continue
        if (c < 1 or c > 3 or r < 1 or r > 3):
            print('Enter numbers within range (1-3)')
            loop = True
        elif (c >= 1 or c <= 3 or r >= 1 or r <= 3) and row[c - 1][r - 1] != ' ':
            print('This position is already taken')
            loop = True
    if p == 1:
        row[c - 1][r - 1] = p1
    else:
        row[c - 1][r - 1] = p2

def check_winner():
    if ' ' not in (row[0][0] , row[1][1] , row[2][2]) and row[0][0] == row[1][1] == row[2][2]: return row[0][0]
    elif ' ' not in (row[0][0] , row[1][1] , row[2][2]) and row[0][0] == row[1][1] == row[2][2]: return row[0][1]
    elif ' ' not in (row[0][2] , row[1][2] , row[2][2]) and row[0][2] == row[1][2] == row[2][2]: return row[0][2]
    elif ' ' not in (row[1][0] , row[1][1] , row[1][2]) and row[1][0] == row[1][1] == row[1][2]: return row[1][0]
    elif ' ' not in (row[2][0] , row[2][1] , row[2][2]) and row[2][0] == row[2][1] == row[2][2]: return row[2][0]
    elif ' ' not in (row[0][0] , row[1][1] , row[2][2]) and row[0][0] == row[1][1] == row[2][2]: return row[0][0]
    elif ' ' not in (row[0][2] , row[1][1] , row[2][0]) and row[0][2] == row[1][1] == row[2][0]: return row[0][2]
    return False


display()
i = 1
while True:
    choice(i)
    display()
    winner = check_winner()
    if winner != False:
        if winner == 'X':
            if p1 == 'X': print('Player 1 wins.')
            else: print('Player 2 wins.')
        else:
            if p1 == 'O': print('Player 1 wins.')
            else: print('Player 2 wins.')
        break
    if i == 1:
        i += 1
    else:
        i -= 1