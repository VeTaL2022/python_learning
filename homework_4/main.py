# 1) Є ось такий файл... ваша задача записати в новий файл тільки
# email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
#
try:
    gmail = 'gmail.com'
    with open('emails.txt') as file, open('resolve-emails.txt', 'w') as resolve:
        for line in file:
            if gmail in line:
                split = line.split()
                resolve.write(f'{split[1]}\n')
except Exception as err:
    print(err)


# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)
#
import json


class Book_of_Purchases:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__purchases_list = []
        self.__id = self.__gen_id()
        self.__read_file()

    def __show_all(self):
        for item in self.__purchases_list:
            print(f'{item["id"]}) {item["name"]} - {item["price"]}')

    def __add(self):
        name = input('Write name: ')

        while True:
            try:
                price = float(input('Write price: '))
                break
            except (Exception,):
                pass
        new_purchase = {'id': next(self.__id), 'name': name, 'price': price}
        self.__purchases_list.append(new_purchase)
        self.__write_file()

    def __find_by(self):
        keys = ['id', 'name', 'price']

        for i, v in enumerate(keys):
            print(f'{i}) {v}')

        choose = input('Choose you want: ')

        if choose.isdigit() and (choose := int(choose) in range(len(keys))):
            # choose = int(choose)
            # if choose in range(len(keys)):
            search = input('Search: ')
            result = next((i for i in self.__purchases_list if i[keys[choose]] == search), None)
            print(result) if result else print('Not Found')
        else:
            print('Error')

    def __most_expensive(self):
        print(max(self.__purchases_list, key=lambda item: item['price']))

    def __delete_by_id(self):
        self.__show_all()
        id = input('Write id: ')

        if id.isdigit():
            id = int(id)
            index = next(({i for i, v in enumerate(self.__purchases_list) if v['id'] == id}), None)

            if index is not None:
                self.__purchases_list.pop(index)
                self.__write_file()
                return
        else:
            print('Error')

    def menu(self):
        while True:
            print('1) Show all')
            print('2) Add')
            print('3) Find by')
            print('4) Most Expensive')
            print('5) Delete by ID')
            print('0) Exit')

            choice = input('Make choice: ')
            print('\n' + '*' * 45)
            match choice:
                case '1':
                    self.__show_all()
                case '2':
                    self.__add()
                case '3':
                    self.__find_by()
                case '4':
                    self.__most_expensive()
                case '5':
                    self.__delete_by_id()
                case '0':
                    break
            print('*' * 45)

    def __gen_id(self):
        id = self.__purchases_list[-1]['id'] + 1 if self.__purchases_list else 0
        while True:
            yield id
            id += 1

    def __read_file(self):
        try:
            with open(self.__file_name) as file:
                self.__purchases_list = json.load(file)
        except (Exception,):
            try:
                with open(self.__file_name, 'w') as file:
                    json.dump(self.__purchases_list, file)
            except Exception as err:
                print(err)

    def __write_file(self):
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__purchases_list, file)
        except Exception as err:
            print(err)


purchases = Book_of_Purchases('purchases.json')
purchases.menu()


# Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# в результат має записатись тільки 5 id
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]

def cut(arr):
    result = []
    gen_array = [(i['id'] for i in item if i['id'] not in result) for item in arr]
    while True:
        for g in gen_array:
            if len(result) == 5:
                return result
            else:
                result.append(next(g))


print(cut(data))
