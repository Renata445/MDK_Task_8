# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

a = [int(i) for i in input().split()]
max = 0
min = 0
for i in range(len(a)):
    if a[i] > a[max]:
        max = i
    if a[i] < a[min]:
        min = i
a[max], a[min] = a[min], a[max]
print(*a)