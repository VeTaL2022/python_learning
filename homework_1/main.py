# 1)Дан list:
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


# - знайти мін число
def find_min():
    print(min(list))


# - видалити усі дублікати
def set_from_list():
    new_list = [*set(list)]
    print(new_list)


# - замінити кожне 4-те значення на 'X'
def swap_x():
    res = []
    for index, element in enumerate(list):
        if (index + 1) % 4 == 0 and index != 0:
            res.append('X')
        else:
            res.append(element)
    print(res)


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(side):
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1 or j == 0 or j == side - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


# 3) вывести табличку множення за допомогою цикла while
def table_of_multi():
    num1 = 1
    while num1 <= 9:
        num2 = 1
        while num2 <= 9:
            result = num1 * num2
            print('  ' if result // 10 else '   ', end='')
            print(result, end='')
            num2 += 1
        num1 += 1
        print()


# 4) переробити це завдання під меню
while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на \'X\'')
    print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('5) вывести табличку множення за допомогою цикла while')
    print('0) - Вихід')
    choice = input('Зробіть вибір: ')
    match choice:
        case '1':
            find_min()
        case '2':
            set_from_list()
        case '3':
            swap_x()
        case '4':
            square(5)
        case '5':
            table_of_multi()
        case '0':
            break
    print('\n')
