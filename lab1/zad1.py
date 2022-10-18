def kupno(artykuły, przedmiot):
    for i in range(len(artykuły)):
        if przedmiot == artykuły[i][0]:
            artykuły[i][1] -= 1


def zwrot(artykuły, przedmiot):
    for i in range(len(artykuły)):
        if przedmiot == artykuły[i][0]:
            artykuły[i][1] += 1


klienci = ["Jan", "Adam", "Paweł", "Jacek"]
sklep = [["skarpety", 10], ["spodnie", 15], ["koszule", 12], ["czapki", 7]]
lista_akcji = []


if __name__ == "__main__":
    while True:
        dane = input("<klient>, [Kupuje/Zwracam], <towar> ")
        klient, akcja, przedmiot = dane.split()
        if akcja == "Kupuje":
            if przedmiot not in sklep[0]:
                print("Nie ma takiego przedmiotu, kup coś innego")
                continue
            kupno(sklep, przedmiot)
            lista_akcji.append(klient, przedmiot, 1)
            print(f'{klient} kupuje {przedmiot}')
            print(sklep)
        if akcja == "Zwracam":
            zwrot(sklep, przedmiot)
        print(lista_akcji)
    for i in range(len(sklep)):
        print(f"Zostały {sklep[i][1]} {sklep[i][0]}")

