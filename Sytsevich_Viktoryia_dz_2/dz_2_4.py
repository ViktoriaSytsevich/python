activity = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for elem in activity:
    name = (elem.split(' '))[-1]
    print (f"'Привет, {name.capitalize()}!'")