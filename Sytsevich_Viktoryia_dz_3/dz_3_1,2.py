dictionary = {
    'ноль': 'zero',
    'один': 'one',
    'два': 'two',
    'три': 'three',
    'четыре': 'four',
    'пять': 'five',
    'шесть': 'six',
    'семь': 'seven',
    'восемь': 'eight',
    'девять': 'nine',
    'десять': 'ten'
}


def num_translate_adv(num):
    if num.istitle() == True:
        num = num.lower()
        return print((dictionary.get(num)).capitalize())
    else:
        return print((dictionary.get(num)))


num_translate_adv((input('num_translate_adv: ')))