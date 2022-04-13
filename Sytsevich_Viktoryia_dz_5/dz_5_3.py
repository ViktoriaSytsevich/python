def generat():
    return ((tutors, klasses[i]) if i < len(klasses) else (tutors, None) for i, tutors in enumerate(tutors))


if __name__ == '__main__':

    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

    gen = generat()
    print(type(gen))
    print(*gen)