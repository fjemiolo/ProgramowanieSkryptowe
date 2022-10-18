import sys


if __name__ == '__main__':
    for arg in sys.argv[1::]:
        option = str(arg)

    data = input()
    if option == "--lista":
        import lista
        lista.zapisz(data)
        lista.wypisz()

    elif option == "--slownik":
        import slownik
        slownik.zapisz(data)
        slownik.wypisz()
