?? ?????? ??????? ?????? ????????? ??????????? ??????? ??????? ?? ?????? ?????? ?? ??????? ??????? ???????? ???????? ?? ??????? ??????. 
????? ?? ??? ???????????, ??? ??? ???????? ????????????
???????
 ?????? ???? ??? ???????? 3 ????? (1. ???? ???????? ?????, 2. ????? ???? ????? ?? ?????? 1, 3. ??????? ????? ?? ?????? 2 ??????? ?????? ??????? ?? 7)

cub = [i**3 for i in range(1, 1001,2)]
print ('cub', cub)
sum_cub = []
for i in cub:
    num = 0
    while i > 0:
        num += i % 10
        i = i // 10
    sum_cub.append(num)
print ('sum_cub', sum_cub)
ind = []
for index, i in enumerate(sum_cub):
    if i % 7 == 0:
        ind.append(index)
print('ind', ind)