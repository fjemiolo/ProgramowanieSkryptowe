import argparse
from datetime import date


class Library:
    def __init__(self):
        self.readers = {}
        self.books = {}

    def borrow(self, line):
        if line[2] in self.books:
            if self.books[line[2]] >= 1:
                self.books[line[2]] -= 1
                if line[0] in self.readers:
                    if line[2] in self.readers[line[0]]:
                        print(f'{line[0]} already has book "{line[2]}"!')
                    else:
                        self.readers[line[0]].append(line[2])
                else:
                    self.readers[line[0]] = []
                    self.readers[line[0]].append(line[2])
            else:
                print(f'Title "{line[2]}" is not currently available.')
        else:
            print(f'Title "{line[2]}" is not available.')

    def return_book(self, line):
         if line[2] in self.books:
            if line[2] in self.readers[line[0]]:
                self.readers[line[0]].remove(line[2])
                self.books[line[2]] += 1
            else:
                print(f'{line[0]} did not borrow "{line[2]}" yet!')
         else:
             print(f'Library did not have title "{line[2]}"!')


    def readFile(self, path):
        with open(path, "r") as f:
            for line in f:
                title, quantity = line.split()
                self.books[title] = int(quantity)

    def parseInputLine(self, line):
        line = line.split()
        if line[1] == "B":
            self.borrow(line)
        if line[1] == "R":
            self.return_book(line)

    def readInput(self):
        while True:
            try:
                line = input("What do you want to do? [Reader [B]orrow/[R]eturn title]: ")
                self.parseInputLine(line)
            except EOFError:

                break

    def summary(self):
        print()
        print("SUMMARY:")
        for person in self.readers:
            print(person, end=" borrowed ")
            for book in self.readers[person]:
                print(f'"{book}"', end=", ")
            print()
        print()
        print("LIBRARY STATUS:")
        for book in self.books:
            print(f'"{book}"', end=" => ")
            print(self.books[book])


if __name__ == "__main__":
    print(str(date.today()))
    parser = argparse.ArgumentParser("Welcome to Library")
    parser.add_argument("file")
    args = parser.parse_args()

    transaction = Library()
    path = args.file
    transaction.readFile(path)
    transaction.readInput()
    transaction.summary()
