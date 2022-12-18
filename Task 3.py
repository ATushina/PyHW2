# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

num = int(input('Введите число: '))
n = []
sum = 0
print(f'Для n={num}: (', end = ' ')
for i in range (1, num):
    n.append((1+1/i)**i)
    sum += n[i-1]
    print(f' {i}: {round(sum, 2)},', end = ' ')
print(f' {num}: {round((sum+(1+1/num)**num), 2)} )')