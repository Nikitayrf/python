'''
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. 
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''

start = int(input('Введите 1-ый элемент арифметической прогресии: '))
step = int(input('Введите разность элементов: '))
length = int(input('Введите сколько будет элементов: '))

for i in range(1, length + 1):
  print(start + (i - 1) * step, end=' ')

