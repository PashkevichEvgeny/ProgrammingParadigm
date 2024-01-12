"""
Условие
    На вход подается число n.
Задача
    Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм.
Пример вывода:
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
..
1 * 9 = 9
"""

# Применена Императивно-структурно-процедурная парадигма
# Императивная - читабельнее код получается
# Структурная - в Python нет goto, вместо него в данной задаче можно использовать цикл for
# Процедурная - дает возможность использовать код повторно при изменении числа n


def multiplication(x):
    for i in range(1, x + 1):
        print(f'1 * {i} = {i}')


multiplication(9)