from random import choice

flag = int(input('Шутки без повтора слов "1", иначе число "2": '))
if flag == 1:
    jokes = int(input('Введите необходимое количество шуток(но не более 5): '))
else:
    jokes = int(input('Введите необходимое количество шуток: '))


def get_jokes():

    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

    for i in range(jokes):
        if flag == 1:
            word_1 = choice(nouns)
            nouns.remove(word_1)
            word_2 = choice(adverbs)
            adverbs.remove(word_2)
            word_3 = choice(adjectives)
            adjectives.remove(word_3)
            print(f'Шутка: {word_1} {word_2} {word_3}')
        else:
            word_1 = choice(nouns)
            word_2 = choice(adverbs)
            word_3 = choice(adjectives)
            print(f'Шутка: {word_1} {word_2} {word_3}')


get_jokes()