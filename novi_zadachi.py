# основные функции

# print()
# input()
# int()
# float()
# str()
# bool()
# list()
# sum()
# min()
# max()
# len()
# sorted()

# Функции без параметров

# def имя_функции():
#   тело_функции

# имя_функции()

# def calc():
#     a = 5
#     b = 10
#     print(a)
#     print(b)
#     # return a + b

# result = calc()
# print(result)
# print(calc())

#pop - udalyaet element spiska po indexu

#Функции с параметрами
# def имя_функции(формальные параметры):
#   тело функции

# имя_функции(фактические параметры)

# var = 10

# def calc_1(a: int, b: int):
#     print(a)
#     print(b)
#     global var
#     var += 10
#     return a + b

# calc_1(3, 6)
# print(var)

# 1 Задача

def is_alive(helth: int):
    if helth > 0:
        print('Ваш персонаж живой')
    else:
        print('Ваш персонаж мертв')

is_alive(1)

# 2 Задача

import random

def arlekin(size):
    chars = input("Введи рандомные числа и буквы и пароль будет сгенирирован: ")
    result = ''
    for i in range(size):
        result += random.choice(chars)
    return result
print(arlekin(10))