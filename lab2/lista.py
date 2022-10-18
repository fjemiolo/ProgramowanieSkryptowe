print('Ładowanie modułu "{0}"'.format(__name__))

############################################

lista = list()


def zapisz(string):
    for sign in string:
        tmp = True
        if '9' >= sign >= '0':
            for number in lista:
                if number[0] == sign:
                    number[1] += 1
                    tmp = False
            if tmp:
                lista.append([sign, 1])


def wypisz():
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    output = ''
    for num in lista:
        output += f"{num[0]}:{num[1]}, "
    print(output)


############################################
print('Załadowano moduł "{0}"'.format(__name__))
