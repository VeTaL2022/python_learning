# 1) написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

# def notebook():
#     todo_list = []
#
#     def add_todo(todo):
#         nonlocal todo_list
#         todo_list += todo
#
#     def get_all():
#         return todo_list
#
#     return [add_todo, get_all]
#
#
# add_new, get_all = notebook()
# print(get_all())
# print('*' * 50)
# add_new(['Помити посуд', 'Позайматися спортом'])
# print(get_all())
# print('*' * 50)
# add_new(['Повчитися'])
# print(get_all())


# 2) протипізувати перше завдання
# from typing import Callable
#
#
# def notebook() -> list[Callable[[str], None] | Callable[[], list]]:
#     todo_list: list = []
#
#     def add_todo(todo: str) -> None:
#         nonlocal todo_list
#         todo_list += todo
#
#     def get_all() -> list:
#         return todo_list
#
#     return [add_todo, get_all]


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді
# строки (також використовуемо типізацію)
# def expanded_form(num: int) -> str:
#     ls: list = []
#     for index, digit in enumerate(str(num)[::-1]):
#         if digit != '0':
#             ls.append(digit + ('0' * index))
#     return ' + '.join(ls[::-1])


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій
# def counter_decor(func):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print('count: ', count)
#         func()
#         print('-' * 20)
#
#     return inner
#
#
# @counter_decor
# def func1():
#     print('func1')
#
#
# @counter_decor
# def func2():
#     print('func2')
#
#
# func1()
# func1()
# func2()
# func1()


# number = int(input())
# count = 0
# for i in range(1, number + 1):
#     if number % i == 0:
#         count += 1
# if count == 2:
#     print('True')
# else:
#     print('False')

# result = []
# a = 10
# for i in range(10, 100):
#     if i == 3 * (a // 10) * (a % 10):
#         result.append(a)
#         a += 1
#     else:
#         a += 1
# print(result)

# i = 0
# while i < 5:
#     print('Hello, while loops!')
#     i += 1

# numbers = [22, 9, 37, 44, 46, 69, 24, 100, 97, 57, 1, 6, 27, 96, 16,
#            82, 10, 95, 99, 78, 62, 50, 77, 86, 56, 40, 49, 32, 53, 76,
#            63, 67, 52, 0, 93, 84, 28, 8, 41, 79, 25, 21, 71, 43, 81, 72,
#            20, 90, 39, 75, 85, 14, 15, 60, 64, 5, 66, 4, 36, 98, 80, 12,
#            47, 91, 73, 45, 31, 65, 87, 74, 11, 34, 33, 18, 58, 23, 68, 94,
#            92, 17, 26, 88, 35, 13, 7, 42, 38, 19, 48, 29, 3, 59, 55, 51, 89,
#            2, 70, 83, 61, 54, 30]
#
# i = 0
# count = 0
# a = numbers
# while i < len(numbers)-1:
#     if numbers[i] > a[i + 1] and numbers[i] > a[i - 1]:
#         count += 1
#     i += 1
#
# print(count)

# start, goal, days = map(int, input().split())
# count_days = 0
# while count_days <= days:
#     if start >= goal:
#         print('True')
#         break
#     else:
#         start *= 1.1
#         count_days += 1
# else:
#     print('False')

# k = int(input())
#
# count = 0
# for c in range(2, k):
#     for b in range(1, c):
#         for a in range(1, b):
#             if a**2 + b**2 == c**2:
#                 count += 1
#
# print(count)

# k = int(input())
# vocabulary = {}
#
# for i in range(0, k):
#     ru, sp = input().split()
#     vocabulary.setdefault(ru, sp)
# word = input()
# print(vocabulary.get(word))


# n, k = map(int, input().split())
# dic = {}
#
# for i in range(n, k + 1):
#     dic.setdefault(i, i**2)
#
# print(dic)

# string = input().lower().split()
# ls = string
# d = {}
# for elem in ls:
#     d.setdefault(elem, elem)
# print(max(d.values()))


# n = int(input())
# dic = {}
# for i in range(n):
#     b, c, d = input().split()
#     dic[b] = int(c) * int(d)
# print(dic[input()])

# numbers = map(int, input().split())
# print(len(set(numbers)))

# numbers = map(int, input().split())
#
# sorted_numbers = sorted(set(numbers))
# print(*sorted_numbers)

# instagram = input().split()
# tiktok = input().split()
# print(len(set(instagram).intersection(set(tiktok))))

# numbers = map(int, input().split())
# duplicate = set()
# num = []
# for i in numbers:
#     n = int(i)
#     if n in duplicate:
#         num.append('yes')
#     else:
#         num.append('no')
#     duplicate.add(n)
# print(' '.join(num))

# numbers = map(int, input().split())
#
#
# def product(numbers):
#     # ваш код
#     n = 1
#     for i in numbers:
#         n *= i
#     return n
#
#
# result = product(numbers)
# print(result)

# number = list(input())
# def product(number):
#     # ваш код
#     if len(number) == 0:
#         return 1
#     else:
#         s = int(number.pop())
#         return s * product(number)
#
#
# result = product(number)
# print(result)
#


# first = map(int, input().split())
# second = map(int, input().split())
# # ваш код
# def mult_list(ls1: list, ls2: list):
#     mult = []
#     for i in range(len(ls1)):
#         element = ls1[i] * ls2[i]
#         mult.append(element)
#     return mult
#
#
# result = mult_list(list(first), list(second))
# print(*result)

# first_word, second_word = input().split()
# # ваш код
# def is_anagram(st1, st2):
#     if sorted(st1) == sorted(st2):
#         return True
#     else:
#         return False
#
# result = is_anagram(first_word, second_word)
# print(result)

# a, b, c = map(int, input().split())
# # ваш код
# def in_interval(num1,num2,num3):
#     if num3 in range(num1,num2+1):
#         return True
#     else:
#         return False
#
# print(in_interval(a, b, c))

# k = int(input())
# s = dict()
# value = tuple()
# for i in range(k):
#     name, age = input().split()
#     s[name] = age
#
# def get_youngest(values):
#     min = 100
#     new_name = ''
#     for name, age in s.items():
#         if min >= int(age):
#             min = int(age)
#             new_name = name
#     return new_name, min
#
# print(*get_youngest(s))

# values = tuple(map(int, input().split()))
#
# def mean(numbers):
#     # n = sum(numbers) / len(numbers)
#     return sum(numbers) / len(numbers)
#
# print(*values,mean(values))

# class User:
#     d = None
#     name = None
#     order = {}
#
#     def __init__(self, identifier, first_name):
#         self.id = identifier
#         self.name = first_name
#
#     def total_sum(self):
#         purchase = 0
#         for item, price in self.order.items():
#             purchase += price
#         return purchase
#
#     def add_purchase(self, item, price):
#         self.order.update({item: price})
#
#     # ваш код
#     def get_orders(self):
#             return ', '.join(list(self.order))
#
# maria = User(10, "Maria")
#
# maria.add_purchase("apple", 20)
# maria.add_purchase("sandwich", 120)
# maria.add_purchase("coffee", 100)
#
# print(maria.get_orders())

class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def checked(self):
        angle1 = angles[0]
        angle2 = angles[1]
        angle3 = angles[2]
        if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
            print('Triangle initialized')
        else:
            print('Initialization failed')


angles = list(map(int, input().split()))
triangle = Triangle(angles[0], angles[1], angles[2])
triangle.checked()
