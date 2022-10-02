# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


# n = input('Введите число: ')
# suma = 0

# for digit in n:
#     if digit.isdigit():
#         suma += int(digit)

# print('Сумма: ', suma)


# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите число: '))
# cnt = 0
# array = []
# start_num = 1
# next_num = 2
# while cnt < number:
#     array.append(start_num)
#     start_num = start_num * next_num
#     cnt += 1
#     next_num += 1
# print(array)


# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072

# num_n = int(input('Введите число N: '))
# temp = 1
# dic = {}
# sum = 0
# for temp in range(1, num_n + 1):
#     dic[temp] = round((1 + 1 / temp) ** temp, 3)
#     sum = sum + dic[temp]
#     temp += 1
# print(dic)
# print(sum)


# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

# num_n = int(input('Введите число N: '))
# list = []
# for i in range(-num_n, num_n + 1):
#     list.append(i)
# print(list)
# position1 = int(input('Укажите первую позицию цифры из списка, которую нужно перемножить: '))
# position2 = int(input('Укажите вторую позицию цифры из списка, которую нужно перемножить: '))
# print(f'Произведение чисел = {list[(position1 - 1)] * list[(position2 - 1)]}')

# Задание 5 Реализуйте алгоритм перемешивания списка.

# def mix_list(list_original):
#     list = list_original[:]
#     list_length = len(list)
#     for i in range(list_length):
#         index_aleatory = random.randint(0, list_length - 1)
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
#     return list


# import random
# list = [random.randint(0,10) for i in range(random.randint(5,20))]
# print(f"Исходный список:\n{list}")
# mixed_list = mix_list(list)
# print("Перемешанный список: ")
# print(mixed_list)