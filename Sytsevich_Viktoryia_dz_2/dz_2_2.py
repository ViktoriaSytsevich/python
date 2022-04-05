sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
length_centence:int = len(sentence)
for elem in range(length_centence):
    elem = sentence.pop(0)
    if elem.isdigit():
        sentence.append(f'"{int(elem):02}"')
    elif elem[0] == '+' and elem[1].isdigit():
        sentence.append(f'"{elem[0]}{int(elem):02}"')
    elif elem[0] == '-' and elem[1].isdigit():
        sentence.append(f'"{int(elem):03}"')
    else:
        sentence.append(elem)
print(' '.join(sentence))