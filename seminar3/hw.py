def check_line(matrix, symbol):
    a = b = 0
    for i in range(3):
        if matrix[i].count(symbol) == 3:
            return True
        if matrix[i][i] == symbol:
            a += 1
        if matrix[i][2 - i] == symbol:
            b += 1
        if a == 3 or b == 3:
            return True
        cnt = 0
        for k in range(3):
            if matrix[k][i] == symbol:
                cnt += 1
            if cnt == 3:
                return True
    return False


m = [[' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ']]


def print_matrix(matrix):
    for i in matrix:
        for k in i:
            print(f'|{k}', end='')
        print()
    print()


def enter_coord(matrix):
    coord = input("Введете координаты квадрата от 1-1 до 3-3: ")
    if coord == 'q':
        print('Game over!')
        exit()
    if len(coord) != 3 or coord not in '1-1-2-2-1-3-3-2-3-1':
        print('Введите значение от 1-1 до 3-3')
        return enter_coord(matrix)
    x, y = map(lambda n: int(n) - 1, coord.split('-'))
    if matrix[x][y] != ' ':
        print('Клетка занята: ')
        return enter_coord(matrix)
    return x, y


cnt = 0
while True:
    x, y = enter_coord(m)
    m[x][y] = 'XO'[cnt % 2]
    cnt += 1
    print_matrix(m)
    for who in 'XO':
        if check_line(m, who):
            print(f'{who} win')
            exit()
