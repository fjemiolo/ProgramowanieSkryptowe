import sys
import getopt

try:
    opt, argument = getopt.getopt(sys.argv[1:], '', ["moduł:="])
except getopt.GetoptError as err:
    print("Wrong parameters!")
    quit()

data = input()
if opt[0][1] == "lista":
    import lista
    lista.zapisz(data)
    lista.wypisz()

elif opt[0][1] == "slownik":
    import slownik
    slownik.zapisz(data)
    slownik.wypisz()
