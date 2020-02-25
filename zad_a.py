import numpy as np


def pierwsze(dane):
    wynik = []
    for x in dane:
        wynik.append(x[-1])
    return list(set(wynik))


typy = []
dane = []
with open('diabetes-type.txt') as plik:
    for linia in plik:
        typy.append((linia.strip().split()))
with open('diabetes.txt') as plik2:
    for linia in plik2:
        dane.append((linia.strip().split()))
xd = pierwsze(dane)
print(xd)
