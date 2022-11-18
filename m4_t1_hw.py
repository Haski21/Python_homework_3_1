"""
Программа получает на вход последовательность целых чисел N(от 1 до 10).
Вам нужно определить вид последовательности:
 - возрастающая
 - убывающая
 - случайная
 - постоянная
В качестве ответа следуют выдать прописными латинскими буквами тип последовательности:
1. ASCENDING (строго возрастающая)
2. WEAKLY ASCENDING (нестрого возрастающая, то есть неубывающая)
3. DESCENDING (строго убывающая)
4. WEAKLY DESCENDING (нестрого убывающая, то есть невозрастающая)
5. CONSTANT (постоянная)
7. RANDOM (случайная)
Примеры входных и выходных данных:
In: 9 4 2 -1  Out: DESCENDING
In: 3 8 8 11  Out: WEAKLY ASCENDING
In: 2 -1 7    Out: RANDOM
In: 5 5 5 5   Out: CONSTANT
"""

str = input('Enter str: ').split()
up = down = middle = 0

for n in range(len(str) - 1):
    if int(str[n]) > int(str[n + 1]):
        down = 1
    elif int(str[n]) < int(str[n + 1]):
        up = 1
    else:
        middle = 1
        
        
if up == 1 and down == middle == 0:
    print('ASCENDING')
elif up == middle == 1 and down == 0:
    print('WEAKLY ASCENDING')
elif down == 1 and up == middle == 0:
    print('DESCENDING')
elif down == middle == 1 and up == 0:
    print('WEAKLY DESCENDING')
elif middle == 1 or middle == 0 and up == down == 0:
    print('CONSTANT')
else:
    print('RANDOM')


























