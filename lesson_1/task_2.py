''' Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) '''

num = int(input("Введите трехзначное число: "))
num_f = num
total = 0
while num != 0:
  last_digit = num % 10
  total += last_digit
  num //= 10
print(f"{total} ({num_f // 100} + {(num_f % 100) // 10} + {num_f % 10})")