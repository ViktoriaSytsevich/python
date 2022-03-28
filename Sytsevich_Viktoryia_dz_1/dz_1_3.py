for i in range(1, 101):
    if i >=11 and i <= 14 or 5<= i % 10 <= 9 or i % 10 == 0:
        print('{} процентов'.format(i))
    elif i % 10 == 1:
        print('{} процент'.format(i))
    elif 2<= i % 10 <= 4:
        print('{} процента'.format(i))