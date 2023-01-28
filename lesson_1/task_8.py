''' Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
3 2 4 -> yes
3 2 1 -> no
'''

n = int(input("Введите число, n-ую сторону дольки: "))
m = int(input("Введите число, m-ую сторону дольки: "))
k = int(input("Введите число, кол-во долек: "))

whole = []
if m == n:
  for i in range(1, m):
    whole.append(n * i)
else:
  for i in range(1, m):
    whole.append(n * i)
  for i in range(1, n):
    whole.append(m * i)

if any(value == k for value in whole):
  print('yes')
else:
  print('no')