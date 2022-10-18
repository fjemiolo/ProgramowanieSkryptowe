def kupno(artykuly, przedmiot, ilosc):
    artykuly[przedmiot] -= ilosc


def zwrot(artykuly, przedmiot, ilosc):
    artykuly[przedmiot] += ilosc


klienci = ["Jan", "Adam", "Paweł", "Jacek"]
sklep = {"jaja": 10, "chleb": 15, "mleko": 12, "sery": 7}
lista_akcji = []


if __name__ == "__main__":
    while True:
        try:
            dane = input("<klient> [kupuje(k)/zwraca(z)] <ilość> <towar>:  ")
            klient, akcja, ilosc, przedmiot = dane.split()
            ilosc = int(ilosc)
            if klient not in klienci:
                klienci.append(klient)

            if akcja == "kupuje" or akcja == "k":
                if przedmiot not in sklep.keys():
                    print("Nie ma takiego przedmiotu, kup coś innego")
                    continue
                elif (sklep[przedmiot] - ilosc) < 0:
                    print("Nie ma wystarczającej ilości tego produktu")
                else:
                    kupno(sklep, przedmiot, ilosc)
                    print(f'{klient} kupił(a) {ilosc} {przedmiot}')
                    lista_akcji.append(f"{klient}: {ilosc} {przedmiot}")

            if akcja == "zwraca" or akcja == "z":
                zwrot(sklep, przedmiot, ilosc)
                print(f'{klient} zwrócił(a) {ilosc} {przedmiot}')

        except:
            print(60*"-")
            print("Wykaz klientów i kupionych przez nich towarów:")
            lista_akcji.sort()
            for i in range(len(lista_akcji)):
                print(lista_akcji[i])
            print(60 * "-")
            print("Stan magazynu: ")
            print(sklep)
            break
