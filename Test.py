import os
os.system('cls')


print('\n1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.' +
      '\nПример:\n- 6782 -> 23\n- 0,56 -> 11')

number = int(input('Введите число: '))
current_number = number
sum = 0

while current_number > 0:
    sum += current_number % 10
    current_number //= 10

print(f'Сумма цифр числа {number} -> {sum}')
