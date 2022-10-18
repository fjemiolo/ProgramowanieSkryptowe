#-*-coding: utf-8-*-

lancuch1 = """ 
To
jest
łańcuch pierwszy."""

lancuch2 = """ 
    A to
    z kolei
    jest łańcuch drugi. :) """

print((lancuch1 + lancuch2) * 3)

print(50 * '-')

lancuch = "Programowanie Skryptowe"
print(lancuch)

print(lancuch[0], lancuch[:2], lancuch[2:], lancuch[-2], lancuch[-3:], lancuch[::2], sep=" | ")

#lancuch[0] = 'X'
#TypeError: 'str' object does not support item assignment
