'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
все те числа, которые встречаются в обоих наборах.Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
'''

len_n = int(input("Введите кол-во элементов множества n: "))
len_m = int(input("Введите кол-во элементов множества m: "))

n = set([int(input("Введите элемент скиска n: ")) for i in range(len_n)])
m = set([int(input("Введите элемент списка m: ")) for i in range(len_m)])
intersection = list(n.intersection(m))

for i in range(len(intersection) - 1):
    if intersection[i] > intersection[i + 1]:
        temp = intersection[i + 1]
        intersection[i + 1] = intersection[i]
        intersection[i] = temp

# 2 Вариант 
# intersection.sort()
print(intersection)


