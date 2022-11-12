# import re

# 1) написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому
# string = 'as 23 fdfdg544'
# result = ','.join([num for num in string if num.isdigit()])
# print(result)
#
# for num in string:
#     if num.isdigit():
#         print(num, end=', ')

# 2) написати прогу яка вибирає зі введеної строки числа і виводить їх так як вони написані
# string = 'as 23 fdfdg544 34'
# res = ''.join(num if num.isdigit() else ' ' for num in string).split()
# print(', '.join(res))
#
# res = re.findall(r'\d+', string)  # або r'-?\d+\.?\d*'
# print(','.join(res))
