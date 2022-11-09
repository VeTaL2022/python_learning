# 1)Дан list:
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# - знайти мін число
# print(min(list))

# - видалити усі дублікати
# new_list = [*set(list)]
# print(new_list)

# - замінити кожне 4-те значення на 'X'
# res = []
# for index, element in enumerate(list):
#     if index % 4 == 0 and index != 0:
#         res.append('X')
#     else:
#         res.append(element)
#
# print(res)

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# def square(side):
#     for i in range(side):
#         for j in range(side):
#             if i == 0 or i == side - 1 or j == 0 or j == side - 1:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         print()
#
# square(6)
