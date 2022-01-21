row1 = [" " for i in range(0, 3)]
row2 = [" " for i in range(0, 3)]
row3 = [" " for i in range(0, 3)]

def print_grid():
    join_row1 = " ".join(map(str,row1))
    join_row2 = " ".join(map(str,row2))
    join_row3 = " ".join(map(str,row3))
    print("---------")
    print("|", join_row1, "|")
    print("|", join_row2, "|")
    print("|", join_row3, "|")
    print("---------")
print_grid()

move_turn = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
def make_a_move():
    global row1, row2, row3, move_turn
    countx = row1.count('X') + row2.count('X') + row3.count('X')
    counto = row1.count('O') + row2.count('O') + row3.count('O')
    sum = countx + counto
    print(sum)
    if row1[0] == row1[1] == row1[2] or\
        row1[0] == row2[0] == row3[0] or\
        row1[0] == row2[1] == row3[2]:
        if row1[0] == 'X' or row1[0] == 'O':
            print(row1[0], 'wins')
            m = row1[0]
            return m
            exit()
    elif row2[0] == row2[1] == row2[2]:
        if row2[0] == 'X' or row2[0] == 'O':
            print(row2[0], 'wins')
            m = row2[0]
            return m
            exit()
    elif row3[0] == row3[1] == row3[2]:
        if row3[0] == 'X' or row3[0] == 'O':
            print(row3[0], 'wins')
            m = row3[0]
            return m
            exit()
    elif row1[1] == row2[1] == row3[1]:
        if row1[1] == 'X' or row1[1] == 'O':
            print(row1[1], 'wins')
            m = row1[1]
            return m
            exit()
    elif row1[2] == row2[2] == row3[2] or\
        row1[2] == row2[1] == row3[0]:
        if row1[2] == 'X' or row1[2] == 'O':
            print(row1[2], 'wins')
            m = row1[2]
            return m
            exit()
    elif sum == 9:
        print('Draw')
        m = 'Draw'
        return m
        exit()
    x, y = input("Enter the coordinates: ").split()
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("You should enter numbers!")
        make_a_move()
    if x < 1:
        print("Coordinates should be from 1 to 3!")
        make_a_move()
    elif y < 1:
        print("Coordinates should be from 1 to 3!")
        make_a_move()
    elif x > 3:
        print("Coordinates should be from 1 to 3!")
        make_a_move()
    elif y > 3:
        print("Coordinates should be from 1 to 3!")
        make_a_move()
    elif x == 1:
        if row1[y-1] != " ":
            print('This cell is occupied! Choose another one!')
            make_a_move()
        else:
            row1[y-1] = move_turn[0]
            move_turn.pop(0)
            print_grid()
            make_a_move()
    elif x == 2:
            if row2[y-1] != " ":
                print('This cell is occupied! Choose another one!')
                make_a_move()
            else:
                row2[y-1] = move_turn[0]
                move_turn.pop(0)
                print_grid()
                make_a_move()
    elif x == 3:
            if row3[y-1] != " ":
                print('This cell is occupied! Choose another one!')
                make_a_move()
            else:
                row3[y-1] = move_turn[0]
                move_turn.pop(0)
                print_grid()
                make_a_move()
make_a_move()
