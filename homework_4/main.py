# 1) Є ось такий файл... ваша задача записати в новий файл тільки
# email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
try:
    gmail = 'gmail.com'
    with open('emails.txt', mode='r') as file, open('resolve.txt', 'w') as resolve:
        for i in file:
            if gmail in i:
                split = i.split()
                resolve.write(f'{split[1]}\n')
except (Exception,):
    pass
