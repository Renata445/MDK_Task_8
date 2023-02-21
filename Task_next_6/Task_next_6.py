# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j

def swap_columns(a, i, j):
    for l in a:
        l[i], l[j]=l[j], l[i]
    return a
n, m=[int(h) for h in input().split()]
a = [[int(j) for j in input().split()] for i in range (n)]
i,j=[int(s) for s in input().split()]
for l in swap_columns(a, i, j):
    print(' '.join([str(i)for i in l]))