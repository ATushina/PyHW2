# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


number = int(input('Введите число N '))
count = 1
mult = 1
while count <= number:
    for i in range(1,number+1):
        mult = mult*i
        print(mult)
        count += 1