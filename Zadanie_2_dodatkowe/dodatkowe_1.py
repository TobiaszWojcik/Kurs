# 1. Masz do dyspozycji generator liczb losowych, który wywołujemy za pomocą funkcji
# random() w ten sposób: liczba_losowa = random().
# [Na górze pliku .py trzeba wstawić linijkę from random import random,
# dlaczego tak, porozmawiamy na następnych zajeciach]. Funkcja random()
# generuje losowe liczby z przedziału od 0 do 1. Przygotuj program,
# który będzie losował N liczb (N podawane przez użytkownika,
# jednak jeżeli poda liczbę większą od 50, poprosimy o podanie mniejszej a jeżeli mniejszej od 0,
# poprosimy o podanie większej),
# podzieli wylosowane liczby pomiędzy 5 przedziałów
# <0, 0.2>,
# (0.2; 0.4>, (0.4; 0.6), <0.6, 0.8), <0.8; 1.0>
# i dla każdego z tych przedziałów po kolei w postaci gwiazdek zaprezentuje liczbę wylosowanych liczb,
# które wpadły do danego przedziału.
#
# Oczekujemy prezentacji wyniku w stylu:
#
# <0.2 *****
# <0.4 ********
# <0.6 **
# <0.8 ****
# <1.0 *******
przedzial_a=0
przedzial_b=0
przedzial_c=0
przedzial_d=0
przedzial_e=0
from random import random
while True:
    try:
        ile_liczb = int(input("Wpisz ile losowych liczb mam wylosować:"))
        if ile_liczb > 50:
            print("To dla mnie za dużo, spróbuj jeszcze raz wpisując mniejszą liczbę!")
        elif ile_liczb < 0:
            print("Taka wartość nie wygeneruje żadnej liczby, spróbuj jeszcze raz wpisując większą liczbę!")
        else:
            break
    except:
        print ("Podana wartość to nie liczba całkowita,spróbuj jeszcze raz")
    print()
for i in range(ile_liczb):
    liczba_losowa = random()
    if liczba_losowa < 0.2:
        przedzial_a += 1
    elif liczba_losowa < 0.4:
        przedzial_b += 1
    elif liczba_losowa < 0.6:
        przedzial_c += 1
    elif liczba_losowa < 0.8:
        przedzial_d += 1
    else:
        przedzial_e += 1
print("<0.2 ", "*"*przedzial_a)
print("<0.4 ", "*"*przedzial_b)
print("<0.6 ", "*"*przedzial_c)
print("<0.8 ", "*"*przedzial_d)
print("<1.0 ", "*"*przedzial_e)