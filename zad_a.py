import numpy as np


def zamiana(dane, typy):
    wynik = []
    dane2 = np.array(dane).transpose()
    i = 0
    while i != np.size(typy, 0):
        if typy[i][1] == 'n':
            wynik.append(strToInt(dane2[i]))
        else:
            wynik.append(dane2[i])
        i += 1
    return np.array(wynik).transpose()


def strToInt(wiersz):
    wynik = []
    for x in wiersz:
        wynik.append(int(x))
    return np.array(wynik).transpose()


def pierwsze(dane):
    wynik = []
    for x in dane:
        wynik.append(x[-1])
    return list(set(wynik))


def drugie(dane):
    wynik = [0, 0]
    pom = pierwsze(dane)
    for x in dane:
        if x[-1] == pom[0]:
            wynik[0] += 1
        else:
            wynik[1] += 1
    return wynik


typy = []
dane = []
with open('diabetes-type.txt') as plik:
    for linia in plik:
        typy.append((linia.strip().split()))
with open('diabetes.txt') as plik2:
    for linia in plik2:
        dane.append((linia.strip().split()))
xd = pierwsze(dane)
xdd = drugie(dane)
dane = zamiana(dane, typy)
print(strToInt(xd))
print(xdd)