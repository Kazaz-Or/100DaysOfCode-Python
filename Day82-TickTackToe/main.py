print('TIC TAC TOE')
print('player 1 symbol = X')
print('player 2 symbol = O\n\n')
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show():
    game = f' {num[0]} | {num[1]} | {num[2]} \n' \
           f'-----------\n' \
           f' {num[3]} | {num[4]} | {num[5]} \n' \
           f'-----------\n' \
           f' {num[6]} | {num[7]} | {num[8]} \n'
    print(game)


show()
p1 = True
n1 = n2 = []
for i in range(9):
    try:
        if p1:
            n = int(input('Player 1 select number: ')) - 1
            if n in n2:
                print('\nNumber {n+1} box already filled by player 2')
            else:
                n1.append(n)
                num[n] = 'X'
                show()
                p1 = False
        else:
            n = int(input('Player 2 select number: ')) - 1
            if n in n1:
                print('\nNumber {n+1} box already filled by player 1')
            else:
                n2.append(n)
                num[n] = 'O'
                show()
                p1 = True
    except ValueError:
        print("\nYou have not typed anything")
    except IndexError:
        print('\nNumber must be between 1 and 9')

    if num[0] == num[1] == num[2] or num[3] == num[4] == num[5] or num[6] == num[7] == num[8] or \
        num[0] == num[3] == num[6] or num[1] == num[4] == num[7] or num[2] == num[5] == num[8] or \
        num[0] == num[4] == num[8] or num[2] == num[4] == num[6]:
        if p1:
            print('Player 2(0) won')
        else:
            print('Player 1(X) won')
        break
    elif i == 8:
        print('Match Draw')
