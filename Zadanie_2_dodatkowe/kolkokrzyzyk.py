import time
import random

"""Gra kolko i krzyżyk!!
Napisz program do gry w kółko i krzyżyk z przeciwnikiem komputerowym. 
Główne założenia:
1. Gracz komputerowy rozpoczyna grę.
2. Gracz komputerowy jest reprezentowany przez krzyżyk.
3. Użytkownik programu jest reprezentowany przez kółko.
4. Przeciwnik komputerowy gra optymalnie, tzn. zawsze wybiera najlepszy 
    możliwy ruch. W połączeniu z pkt 1 oznacza to, że gracz komputerowy
    nigdy nie przegra.
5.Identyfikatory pól na tablicy są rozmieszczone następująco:
   1 2 3
   4 5 6
   7 8 9 .

Przebieg gry (działanie programu):
1. Przeciwnik komputerowy wykonuje ruch. Jeśli komputer wygrał,
    wyświetla komunikat "Przegrana". Jeśli ostatnie pole zostało wypełnione,
    wyświetla komunikat "Remis" i kończy działanie.
2. Program zaczyna działanie od wyświetlenia tablicy jako trzech linii
    w terminalu. Minus "-" symbolizuje pole jeszcze nie wypełnione.
---
-X-
---
3. Program pobiera od użytkownika identyfikator pola,
które ma być wypełnione kółkiem i oczekuje naciśnięcia <Enter>.
4. Jeśli identyfikator pola jest nieprawidłowy (zły identyfikator lub pole jest
    już zajęte), program wyświetla napis "Błąd", i wraca do punktu 4.
5. Program wraca do punktu 1."""
DO_TEST = False


# Funkcja wyświetlając napisy zależna od stałej do_test
def test(tekst):
    if DO_TEST:
        print(tekst)


# Funkcja rysująca planszę gry
def rysuj_plansze(plansza, pozostale=False):
    idx = 1
    for y in range(3):
        for x in range(3):
            if plansza[idx] == 0:
                if pozostale:
                    print(idx, end="")
                else:
                    print("-", end="")
            elif plansza[idx] == 1:
                if pozostale:
                    print(end=" ")
                else:
                    print("O", end="")
            else:
                if pozostale:
                    print(end=" ")
                else:
                    print("X", end="")
            idx += 1
        print()


# Funkcja sprawdzająca kto wygrał rozgrywkę
def przegrana():
    if gracz:
        print("Przegrałeś!!")
    else:
        print("Wygrałeś")
    stangry[0] = 0


stangry = [1,
           2, 1, 1,
           0, 2, 0,
           0, 0, 2]

rysuj_plansze(stangry)

input("Aby zagrać naciśnij <Enter>")

gra = 9
stangry = [1,
           0, 0, 0,
           0, 0, 0,
           0, 0, 0]
gracz = False
ruch_gracza = 0

rysuj_plansze(stangry)

while gra:
    print()
    if gracz:

        rysuj_plansze(stangry, True)

        ruch_gracza = input("Wpisz cyfrę odpowiadającą polu! ")
        try:
            ruch_gracza = int(ruch_gracza)
            if (ruch_gracza >= 1) and (ruch_gracza <= 9):
                if stangry[ruch_gracza] == 0:
                    gra -= 1
                    if gracz:
                        stangry[ruch_gracza] = 1
                    else:
                        stangry[ruch_gracza] = 2
                    gracz = not gracz
                else:
                    print("To pole jest już zajęte!")
            else:
                print("Podałeś złą wartość!")

        except:
            print("Podałeś złą wartość!")
    else:

        # Algorytm ruchu komputera
        if gra == 9:
            print("Zaczyna komputer!")
            stangry[5] = 2
        else:
            print("Teraz kolej komputera!")
        time.sleep(1)
        warunek = True

        # Sprawdzanie wierszy
        if warunek:
            test("Warunek 1 - sprawdzanie")
            for i in range(0, 9, 3):
                if (stangry[1 + i]
                    + stangry[2 + i]
                    + stangry[3 + i]) == 4 and (
                        stangry[1 + i] == 0 or
                        stangry[2 + i] == 0 or
                        stangry[3 + i] == 0):
                    test("Warunek 1 - znalazło")
                    if stangry[1 + i] == 0:
                        stangry[1 + i] = 2
                    elif stangry[2 + i] == 0:
                        stangry[2 + i] = 2
                    else:
                        stangry[3 + i] = 2
                    warunek = False
                    break

        # Sprawdzanie kolumn
        if warunek:
            test("Warunek 2 - sprawdzanie")
            for i in range(0, 3):
                if (stangry[1 + i]
                    + stangry[4 + i]
                    + stangry[7 + i]) == 4 and (
                        stangry[1 + i] == 0 or
                        stangry[4 + i] == 0 or
                        stangry[7 + i] == 0):
                    test("Warunek 2 - znalazło")
                    if stangry[1 + i] == 0:
                        stangry[1 + i] = 2
                    elif stangry[4 + i] == 0:
                        stangry[4 + i] = 2
                    else:
                        stangry[7 + i] = 2
                    warunek = False
                    break

        # Sprawdzanie przekątnych
        if warunek:
            test("Warunek 3 - sprawdzanie")
            if (stangry[1] + stangry[9]) == 2 and (
                    stangry[1] == 0 or
                    stangry[9] == 0):
                test("Warunek 3a - znalazło")

                if stangry[1] == 0:
                    stangry[1] = 2
                else:
                    stangry[9] = 2
                warunek = False
            elif (stangry[3] + stangry[7]) == 2 and (
                    stangry[3] == 0 or
                    stangry[7] == 0):
                test("Warunek 3b - znalazło")
                if stangry[3] == 0:
                    stangry[3] = 2
                else:
                    stangry[7] = 2
                warunek = False

        # Sprawdzanie czy przeciwnik nie ma szansy wygrania w następnym ruchem
        if warunek:
            test("Warunek 6 - sprawdzanie")
            if ruch_gracza != 0:
                if ruch_gracza % 2 == 0:
                    if ruch_gracza == 2 or ruch_gracza == 8:
                        if (stangry[ruch_gracza - 1]
                                + stangry[ruch_gracza]
                                + stangry[ruch_gracza + 1]) == 2:
                            test("Warunek 4a - znalazło")
                            if stangry[ruch_gracza - 1] == 1:
                                stangry[ruch_gracza + 1] = 2
                            else:
                                stangry[ruch_gracza - 1] = 2
                            warunek = False
                    else:
                        if (stangry[ruch_gracza - 3]
                                + stangry[ruch_gracza]
                                + stangry[ruch_gracza + 3]) == 2:
                            test("Warunek 4b - znalazło")
                            if stangry[ruch_gracza - 3] == 1:
                                stangry[ruch_gracza + 3] = 2
                            else:
                                stangry[ruch_gracza - 3] = 2
                            warunek = False
                else:
                    if ruch_gracza % 3 == 0:
                        if (stangry[ruch_gracza - 1]
                                + stangry[ruch_gracza]
                                + stangry[ruch_gracza - 2]) == 2:
                            test("Warunek 4c - znalazło")
                            if stangry[ruch_gracza - 1] == 1:
                                stangry[ruch_gracza - 2] = 2
                            else:
                                stangry[ruch_gracza - 1] = 2
                            warunek = False
                    else:
                        if (stangry[ruch_gracza + 1]
                                + stangry[ruch_gracza]
                                + stangry[ruch_gracza + 2]) == 2:
                            test("Warunek 4d - znalazło")
                            if stangry[ruch_gracza + 1] == 1:
                                stangry[ruch_gracza + 2] = 2
                            else:
                                stangry[ruch_gracza + 1] = 2
                            warunek = False
                    if warunek:
                        test("Warunek 5 - sprawdzanie")
                        if ruch_gracza > 3:
                            if (stangry[ruch_gracza - 3]
                                    + stangry[ruch_gracza]
                                    + stangry[ruch_gracza - 6]) == 2:
                                test("Warunek 5a - znalazło")
                                if stangry[ruch_gracza - 3] == 1:
                                    stangry[ruch_gracza - 6] = 2
                                else:
                                    stangry[ruch_gracza - 3] = 2
                                warunek = False
                        else:
                            if (stangry[ruch_gracza + 3]
                                    + stangry[ruch_gracza]
                                    + stangry[ruch_gracza + 6]) == 2:
                                test("Warunek 5b - znalazło")
                                if stangry[ruch_gracza + 6] == 1:
                                    stangry[ruch_gracza + 3] = 2
                                else:
                                    stangry[ruch_gracza + 6] = 2
                                warunek = False
        if warunek:
            test("Warunek 6 - sprawdzanie")
            sprawdz_pola = []
            for idx in range(1, 10):
                if stangry[idx] == 0:
                    sprawdz_pola.append(idx)

            test(sprawdz_pola)
            random_sprawdz_pole = []
            ile_zostalo = len(sprawdz_pola)
            test("Tyle powinno razy losować {}".format(ile_zostalo))
            for idx in range(ile_zostalo):
                test(len(sprawdz_pola))
                losowa = random.randint(0, len(sprawdz_pola)-1)
                test("Tojest losowa {}".format(losowa))
                wstaw_to = sprawdz_pola.pop(losowa)
                test("to wstawiam {}".format(wstaw_to))
                test("to pozostało {}".format(sprawdz_pola))
                random_sprawdz_pole.append(wstaw_to)
            test(random_sprawdz_pole)
            random_filled = random.randint(0, len(sprawdz_pola))
            for idx in random_sprawdz_pole:
                if idx != 0:
                    if idx % 2 == 0:
                        if idx == 2 or idx == 8:
                            if (stangry[idx - 1]
                                    + stangry[idx]
                                    + stangry[idx + 1]) == 1:
                                test("Warunek 4a - znalazło")
                                stangry[idx] = 2
                                warunek = False
                                break
                        else:
                            if (stangry[idx - 3]
                                    + stangry[idx]
                                    + stangry[idx + 3]) == 1:
                                test("Warunek 4b - znalazło")
                                stangry[idx] = 2
                                warunek = False
                                break
                    else:
                        if idx % 3 == 0:
                            if (stangry[idx - 1]
                                    + stangry[idx]
                                    + stangry[idx - 2]) == 1:
                                test("Warunek 4c - znalazło")
                                stangry[idx] = 2
                                warunek = False
                                break
                        else:
                            if (stangry[idx + 1]
                                    + stangry[idx]
                                    + stangry[idx + 2]) == 1:
                                test("Warunek 4d - znalazło")
                                stangry[idx] = 2
                                warunek = False
                                break
                        if warunek:
                            test("Warunek 5 - sprawdzanie")
                            if idx > 3:
                                if (stangry[idx - 3]
                                        + stangry[idx]
                                        + stangry[idx - 6]) == 2:
                                    test("Warunek 5a - znalazło")
                                    stangry[idx] = 2
                                    warunek = False
                                    break
                            else:
                                if (stangry[idx + 3]
                                        + stangry[idx]
                                        + stangry[idx + 6]) == 2:
                                    test("Warunek 5b - znalazło")
                                    stangry[idx] = 2
                                    warunek = False
                                    break

        if ruch_gracza == 0:
            stangry[5] = 2
            warunek = False

        if warunek:
            test("Warunek 7 - sprawdzanie")
            while True:
                liczba_losowa = round(random.random() * 9)
                if stangry[liczba_losowa] == 0:
                    test("Warunek 6 - znalazło")
                    stangry[liczba_losowa] = 2
                    break
        gra -= 1
        gracz = not gracz

    if stangry[1] == stangry[2] == stangry[3] > 0:
        przegrana()
    elif stangry[4] == stangry[5] == stangry[6] > 0:
        przegrana()
    elif stangry[7] == stangry[8] == stangry[9] > 0:
        przegrana()
    elif stangry[1] == stangry[4] == stangry[7] > 0:
        przegrana()
    elif stangry[2] == stangry[5] == stangry[8] > 0:
        przegrana()
    elif stangry[3] == stangry[6] == stangry[9] > 0:
        przegrana()
    elif stangry[1] == stangry[5] == stangry[9] > 0:
        przegrana()
    elif stangry[3] == stangry[5] == stangry[7] > 0:
        przegrana()

    if stangry[0] == 0:
        rysuj_plansze(stangry)
        break

    rysuj_plansze(stangry)
else:
    print()
    rysuj_plansze(stangry)
    print()
    print("REMIS!!")
