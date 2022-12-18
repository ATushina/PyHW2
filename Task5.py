#Реализуйте алгоритм перемешивания списка.

import random
s = input('введите числа через пробел  ').split()
random.shuffle(s)
print(s)