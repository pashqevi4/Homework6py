# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

N = int(input())
list_1 = []
for i in range(N):
    list_1.append(randint(1, 50))

print(*list_1)

x = int(input())
y = int(input())
if x > y:
    x, y = y, x

list_2 = []

for i in range(N):
    if x <= list_1[i] <= y:
        list_2.append(i)

print(*list_2)