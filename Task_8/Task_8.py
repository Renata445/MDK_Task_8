# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

a = [int(i) for i in input().split()]
numbers_various = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        numbers_various += 1
print(numbers_various)
