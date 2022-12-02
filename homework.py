import math
from itertools import *
from random import randint
from sympy import Poly
from sympy.abc import x
import os


# Домашняя работа к семинару 4, для выбора необходимой программы запустите код и введите номер программы для проверки.

# Задача 1 Вычислить число c заданной точностью d
def ProgramOne():
    accuracy = input('Введите точность в формате "0.01", либо введите число знаков после запятой = ')
    if '.' not in accuracy:
        print(f'Число Pi с заданной точностью = {round(math.pi, int(accuracy))}')
    else:
        accuracy = str(accuracy.split('.')[1])
        print(f'Число Pi с заданной точностью = {round(math.pi, len(accuracy))}')
    MainProgram()


# Задача 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def ProgramTwo():
    num = int(input('Ввеите натуральное число = '))
    number = num
    multiplier = 2
    listMultipliers = [1]
    while multiplier <= num:
        if num % multiplier == 0:
            listMultipliers.append(multiplier)
            num //= multiplier
        else:
            multiplier += 1
    print(f'Список простых множителей для числа {number} = {listMultipliers}')
    MainProgram()


# Задача 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
def ProgramThree():
    listNumbers = list(map (int, str(input('Введите последовательность чисел через пробел = ')).split()))
    newList = []
    for i in listNumbers:
        if i not in newList:
            newList.append(i)
    print(newList)
    MainProgram()


# Задача 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
def GetPolynomial(k):
    list = []
    for i in range(k):
        list.append(randint(1, 10))
    print(f'Список случайных значений переменных = {list}')
    polynomial = ''
    count = 1
    for i in list:
        if count < len(list):
            polynomial = polynomial + f'{i}*x**{k} + '
        else:
            polynomial = polynomial + f'{i}'
        k -= 1
        count += 1
    return polynomial


def ProgramFour():
    k = int(input('Введите натуральную степень k для первого многочлена = '))
    k2 = int(input('Введите натуральную степень k для второго многочлена = '))
    firstPolynomial = GetPolynomial(k)
    fileOne = open('polynomialOne.txt', 'w')
    fileOne.write(firstPolynomial)
    secondPolynomial = GetPolynomial(k2)
    fileOne.close()
    fileTwo = open('polynomialTwo.txt', 'w')
    fileTwo.write(secondPolynomial)
    fileTwo.close()
    print(f'Первый многочлен равен = {firstPolynomial.replace("**", "^")}')
    print(f'Второй многочлен равен = {secondPolynomial.replace("**", "^")}')
    MainProgram()


# Задача 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.
def ProgramFive():
    fileOne = open('polynomialOne.txt', 'r').readline()
    fileTwo = open('polynomialTwo.txt', 'r').readline()
    print(f'Первый многочлен равен = {fileOne.replace("**", "^")}')
    print(f'Второй многочлен равен = {fileTwo.replace("**", "^")}')
    sumPolynomial = str(Poly(fileOne, x) + Poly(fileTwo, x))
    sumPolynomial = sumPolynomial.split(',')[0]
    sumPolynomial = sumPolynomial.replace('Poly(', '').replace("**", "^")
    print(f'Сумма многочленов = {str(sumPolynomial)}')
    MainProgram()


# Основная программа
def MainProgram():
    print('Введите номер программы (1-5), либо введите "Q" для выхода.')
    program = input('Программа № = ')
    if program.lower() == 'q':
        print('До свидания!')
    elif program.isdigit():
        if int(program) == 1:
            ProgramOne()
        elif int(program) == 2:
            ProgramTwo()
        elif int(program) == 3:
            ProgramThree()
        elif int(program) == 4:
            ProgramFour()
        elif int(program) == 5:
            ProgramFive()
        else:
            print('Введен некорректный номер, попробуйте еще раз.')
            MainProgram()
    else:
        print('Ввод некорректен, пожалуйста, попробуйте еще раз.')
        MainProgram()


print('Здравствуйте!')
MainProgram()
