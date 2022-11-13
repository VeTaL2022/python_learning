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
