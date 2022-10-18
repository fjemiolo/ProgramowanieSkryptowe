print('Ładowanie modułu "{0}"'.format(__name__))

############################################

slownik = dict()


def zapisz(string):
    for sign in string:
        if '9' >= sign >= '0':
            if sign in slownik:
                slownik[sign] += 1
            else:
                slownik[sign] = 1


def wypisz():
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    output = ''
    for num in sorted(slownik):
        output += f"{num}:{slownik[num]}, "
    print(output)


############################################
print('Załadowano moduł "{0}"'.format(__name__))
