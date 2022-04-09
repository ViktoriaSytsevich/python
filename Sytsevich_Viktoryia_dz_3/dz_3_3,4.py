def thesaurus_adv(*args):
    names_dict = {}
    for elem in args:
        name, second_name = elem.split()
        if not names_dict.get(second_name[0]):
            names_dict[second_name[0]] = { name[0] : [elem] }
        elif not names_dict[second_name[0]].get(name[0]):
            (names_dict[second_name[0]])[name[0]] = [elem]
        else:
            (names_dict[second_name[0]])[name[0]].append(elem)

    return dict(sorted(names_dict.items()))


print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))