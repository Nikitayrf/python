'''
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

def pow_num(num, pow = 0):
  if pow <= 1:
    return num
  return num * pow_num(num, pow - 1)

print(pow_num(a, b))