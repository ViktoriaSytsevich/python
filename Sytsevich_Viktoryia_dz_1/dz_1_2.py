cub = [i**3 for i in range(1, 1001,2)]
print ('Список кубов нечётных чисел', cub)
sum_cub = []
for i in cub:
    if sum(map(int,str(i))) % 7 ==0:
        sum_cub.append(i)
print ('Числа - сумма цифр которых делится нацело на 7', sum_cub)
result = sum(sum_cub)
print ('1. Сумма =', result)
cub_17 = [i**3+17 for i in range(1, 1001,2)]
print ('Список кубов нечётных чисел +17', cub_17)
sum_cub_17 = []
for i in cub_17:
    if sum(map(int,str(i))) % 7 ==0:
        sum_cub_17.append(i)
print ('Числа - сумма цифр которых делится нацело на 7', sum_cub_17)
result_17 = sum(sum_cub_17)
print ('2. Сумма =', result_17)