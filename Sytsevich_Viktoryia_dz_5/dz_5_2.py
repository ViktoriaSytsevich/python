n = int(input('Введите n: '))
odd_to_n = [i for i in range (1, n + 1, 2)]
#odd_to_n = [i for i in range (1, n + 1) if i % 2 == 1]
for i in odd_to_n:
    print(i)