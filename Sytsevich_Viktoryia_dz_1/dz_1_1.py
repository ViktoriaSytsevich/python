sec = int(input('duration = '))
if sec < 60:
    print(sec, 'сек')
elif sec >= 60 and sec < 3600:
    if sec%60 != 0:
        print(sec//60, 'мин', sec%60, 'сек')
    else:
        print(sec // 60, 'мин')
elif sec >= 3600 and sec < 86400:
    hour = sec//3600
    min = sec%3600//60
    sec = sec%3600%60
    if min == 0 and sec == 0:
        print(hour, 'час')
    elif min != 0 and sec == 0:
        print(hour, 'час', min, 'мин')
    elif min == 0 and sec != 0:
        print(hour, 'час', sec, 'сек')
    else:
        print(hour, 'час', min, 'мин', sec, 'сек')
else:
    day = sec//86400
    hour = sec%86400//3600
    min = sec%86400%3600//60
    sec = sec%86400%3600%60
    if hour == 0 and min == 0 and sec == 0:
        print (day, 'дн')
    elif min == 0 and sec == 0:
        print (day, 'дн', hour, 'час')
    elif sec == 0:
        print(day, 'дн', hour, 'час', min, 'мин')
    elif hour ==0:
        print(day, 'дн', min, 'мин', sec, 'сек')
    elif hour == 0 and sec == 0:
        print (day, 'дн', min, 'мин')
    elif hour == 0 and min == 0:
        print (day, 'дн', sec, 'сек')
    else:
        print(day, 'дн', hour, 'час', min, 'мин', sec, 'сек')
