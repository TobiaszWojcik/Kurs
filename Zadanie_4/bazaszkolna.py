"""
Mamy trzy typy użytkowników:

Wychowawca - ma przypisane klasy
Nauczyciel - Mentor ma przypisany przedmiot i wiele klas
Uczeń - jest przypisany do jednej klasy

Napisz program, który ze standardowego wyjścia pobierze dane w następujący sposób:

Pobierze typ użytkownika: (uczeń, nauczyciel, wychowawca, koniec), oraz Imię i nazwisko Jeśli pobrano koniec, przejdź do kroku 5
Jeśli typ użytkownika to uczeń, pobierz jedną linię - będzie to nazwa klasy (np. 3C), przejdź do kroku 1
Jeśli typ użytkownika to nauczyciel, pobierz 1 linię - nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, aż do otrzymania pustej linii. Przejdź do korku 1
Jeśli typ użytkownika to wychowawca, pobieraj w nowych liniach nazwy klas, które prowadzi wychowawca, aż do pustej linii, przejdź do kroku 1
Wykonaj polecenie na podstawie przekazanego argumentu

Program będzie wykonywany w następujący sposób (zakładając nazwę pliku bazaszkolna.py)
python bazaszkolna.py <phrase>
jeśli phrase to nazwa klasy: program wypisze wychowawcę i uczniów w klasie
jeśli phrase to wychowawca: wypisz wszystkich uczniów, których prowadzi wychowawca
jeśli phrase to nauczyciel: wypisz wychowawców wszystkich klas, z którym ma zajęcia nauczyciel
jeśli phrase to uczeń: wypisz wszystkie lekcje, które ma uczeń i nauczycieli, którzy je prowadzą
"""
def take_groups():
    groups = []
    while True:
        take_group = input()
        if take_group = "":
            break
        else:
            groups.append(take_group)
    return groups


class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

class Teacher:
    def __init__(self, name, groups, subject):
        self.name = name
        self.groups = groups
        self.subject = subject

class Preceptor:
    def __init__(self, name, groups):
        self.name = name
        self.groups = groups

students = []
teache
status = True

while status:
    take_data = str(input())
    if take_data == "wychowawca":
        name
    elif take_data == "nauczyciel":
        pass
    elif take_data == "uczen":

    elif take_data == "koniec":
        status = False
    else:
        break

else:
    pass