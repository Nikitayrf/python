'''
Петя успевает по математике лучше всех в классе, поэтому учитель задал ему сложное домашнее задание, в котором нужно в заданном наборе целых чисел найти сумму всех положительных элементов, затем найти где в заданной последовательности находятся максимальный и минимальный элемент и вычислить произведение чисел, расположенных в этой последовательности между ними. Так же известно, что минимальный и максимальный элемент встречаются в заданном множестве чисел только один раз и не являются соседними. Поскольку задач такого рода учитель дал Пете около ста, то Петя как сильный программист смог написать программу, которая по заданному набору чисел самостоятельно находит решение. А Вам слабо?
'''

def sum(list_sum):
    summ = 0
    for i in list_sum:
        if i > 0:
            summ += i
    return summ

def i_minmax(list_i):
    tmin = list_i[0]
    tmax = list_i[0]
    imin = 0
    imax = 0
    for i in range(1, len(list_i)):
        if list_i[i] <= tmin:
            tmin = list_i[i]
            imin = i
        if list_i[i] >= tmax:
            tmax = list_i[i]
            imax = i
    return imin, imax

def product_between_minmax(i_min, i_max, list_minmax):
    list_product = list()
    if i_min < i_max:
        list_product = list_minmax[i_min + 1: i_max]
    else:
        list_product = list_minmax[i_max + 1: i_min]

    product = 1
    for i in list_product:
        product *= i
    return product

n = int(input("Введите длину списка: "))
list_inp = [int(input(f'введите {i}-ой элемент списка: ')) for i in range(n)]

print(sum(list_inp), product_between_minmax(i_minmax(list_inp)[0], i_minmax(list_inp)[1], list_inp), end=' ')