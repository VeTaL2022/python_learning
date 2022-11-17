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
#     def __init__(self, x: int, y: int) -> None:
#         self.x = x
#         self.y = y
#         self.area = x * y
#
#     def __add__(self, other) -> int:
#         return self.area + other.area
#
#     def __sub__(self, other) -> int:
#         return self.area - other.area
#
#     def __eq__(self, other) -> bool:
#         return self.area == other.area
#
#     def __neq__(self, other) -> bool:
#         return self.area != other.area
#
#     def __gt__(self, other) -> bool:
#         return self.area > other.area
#
#     def __lt__(self, other) -> bool:
#         return self.area < other.area
#
#     def __len__(self) -> int:
#         return self.x + self.y
#
#
# rectangle1 = Rectangle(4, 7)
# rectangle2 = Rectangle(3, 9)
# print(' + ', rectangle1 + rectangle2)
# print(' - ', rectangle1 - rectangle2)
# print(' == ', rectangle1 == rectangle2)
# print(' != ', rectangle1 != rectangle2)
# print(' > ', rectangle1 > rectangle2)
# print(' < ', rectangle1 < rectangle2)
# print('sum of sides = ',len(rectangle1))
# print('sum of sides = ',len(rectangle2))


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
#     def __init__(self, name: str, age: int) -> None:
#         self.age = age
#         self.name = name
#
#
# class Prince(Human):
#     def __init__(self, name: str, age: int, size_of_founded_shoe: float) -> None:
#         super().__init__(name, age)
#         self.size_of_founded_shoe = size_of_founded_shoe
#
#     def find_cinderella(self, all_cinderellas: list[str]) -> None:
#         for i in all_cinderellas:
#             if self.size_of_founded_shoe == i.size_of_shoe:
#                 print(f'prince `{self.name}` and cinderella `{i.name}` => Couple :)')
#
#
# class Cinderella(Human):
#     count: int = 0
#
#     def __init__(self, name: str, age: int, size_of_shoe: float) -> None:
#         super().__init__(name, age)
#         self.size_of_shoe = size_of_shoe
#
#     @classmethod
#     def count_all(cls) -> None:
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
# from abc import ABC, abstractmethod
#
#
# class Printable(ABC):
#     @abstractmethod
#     def print(self) -> None:
#         pass
#
#
# # 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# class Book(Printable):
#     def __init__(self, name: str) -> None:
#         self.name = name
#
#     def print(self) -> None:
#         print(self.name)
#
#
# class Magazine(Printable):
#     def __init__(self, name: str) -> None:
#         self.name = name
#
#     def print(self) -> None:
#         print(self.name)
#

# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додав
# ати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# class Main:
#     printable_list: list = [str]
#
#     def add(self) -> None:
#         if isinstance(self, Magazine):
#             Main.printable_list.append(self)
#         elif isinstance(self, Book):
#             Main.printable_list.append(self)
#
#     @staticmethod
#     def show_all_magazines() -> None:
#         for magazines in Main.printable_list:
#             if isinstance(magazines, Magazine):
#                 magazines.print()
#
#     @staticmethod
#     def show_all_books() -> None:
#         for books in Main.printable_list:
#             if isinstance(books, Book):
#                 books.print()
#
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Book('Book3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
