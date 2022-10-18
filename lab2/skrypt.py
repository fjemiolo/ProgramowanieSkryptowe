# -*-coding: utf-8-*-

import re


def func(string):
    numbers = re.findall('[0-9]+', string)
    words = re.findall('[a-zA-ZąęćśńźóżłĄĘŚŃŹÓŻŁ]+', string)
    if len(numbers) > 0:
        print("Liczba:", *numbers)
    if len(words) > 0:
        print("Wyraz:", *words)


if __name__ == "__main__":
    while True:
        try:
            data = input()
        except:
            break
        func(data)
