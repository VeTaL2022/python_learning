# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
#
# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.res = x * y / 2
#
#     def __add__(self, other):
#         return self.res + other.res
#
#     def __sub__(self, other):
#         return self.res - other.res
#
#     def __eq__(self, other):
#         return self.res == other.res
#
#     def __neq__(self, other):
#         return self.res != other.res
#
#     def __gt__(self, other):
#         return self.res > other.res
#
#     def __lt__(self, other):
#         return self.res < other.res
#
#     def __len__(self):
#         return self.x + self.y
#
#
# rectangle1 = Rectangle(2, 2)
# rectangle2 = Rectangle(1, 1)
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle2)
# print(rectangle1 > rectangle2)
# print(rectangle1 < rectangle2)
# print(len(rectangle1))
# print(len(rectangle2))


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка,
# а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
#
# class Human:
#     __slots__ = ('name', 'age')
#
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#
# class Prince(Human):
#     def __init__(self, name, age, size_of_founded_shoe):
#         super().__init__(name, age)
#         self.size_of_founded_shoe = size_of_founded_shoe
#
#     def find_cinderella(self, all_cinderellas):
#         for i in all_cinderellas:
#             if self.size_of_founded_shoe == i.size_of_shoe:
#                 print(f'prince `{self.name}` and cinderella `{i.name}` => Couple :)')
#
#
# class Cinderella(Human):
#     count = 0
#
#     def __init__(self, name, age, size_of_shoe):
#         super().__init__(name, age)
#         self.size_of_shoe = size_of_shoe
#
#     @classmethod
#     def count_all(cls):
#         print('The number of class instances created = ', cls.count)
#
#
# cinderellas = [
#     Cinderella('Jaq', 51, 39.5), Cinderella('Gus', 24, 37), Cinderella('Suzy', 18, 36.2),
#     Cinderella('Perla', 17, 35), Cinderella('Drizella', 58, 40.4), Cinderella('Anastasia', 22, 37),
#     Cinderella('Kate', 19, 36.6), Cinderella('Lady Tremaine', 10, 31), Cinderella('Cinderella', 14, 37.5)
# ]
# for cinderella in cinderellas:
#     Cinderella.count += 1
#
# Cinderella.count_all()
#
# prince = Prince('Kevin', 24, 35)
# prince.find_cinderella(cinderellas)


# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
#
class Printable:
    def print(self):
        return self.print()


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
class Book(Printable):
    def __init__(self, name):
        self.name = name


class Magazine(Printable):
    def __init__(self, name):
        self.name = name


# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додав
# ати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
class Main(Book, Magazine):
    printable_list = []

    def add(self):
        Main.printable_list.append(Book(self.name))
        Main.printable_list.append(Magazine(self.name))

    def show_all_magazines(self):
        self.print()

    def show_all_books(self):
        self.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
