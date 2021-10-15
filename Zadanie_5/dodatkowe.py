# Funkcje
# Stwórz funkcję, która przyjmuje dwie liczby całkowite, które są granicami przedziału
# liczbowego i zwraca informację czy w tym przedziale są liczby podzielne przez 3
# i ile jest tam takich liczb. Przykładowo func(1,7) zwróci (True, 2).

# Klasy
# Stwórz klasę pies, wiedząc, że pies może mieć charakterystyczne imię, rasę, kolor sierści,
# a ponadto powinien móc szczekać i wyć.

class Pies():
    def __init__(self, imie, rasa, kolor_siersci):
        self.imie = imie
        self.rasa = rasa
        self.kolor_siersci = kolor_siersci

    def szczekaj(self):
        print("Hał Hał")

    def wyj(self):
        print("Auuuuuuu")

pies = Pies("Reksio", "kundel", "łaciaty")
pies.szczekaj()
pies.wyj()

# Stwórz klasę betoniarka. Betoniarka ma swoją charakterystyczną pojemność (w litrach)
# Betoniarka może być podłączona lub może nie być podłączona do prądu, powinna mieć funkcję wyłączenia.
# Betoniarka może, ale nie musi zostać napełniona piachem, cementem i wodą.
# Betoniarka przygotuje i wyrzuci cement tylko wtedy, gdy ma zarówno wodę,
# jak i cement, i piach. Dodatkowo: betoniarka wyższej klasy informuje o jakości cementu, gdy
# go wyrzuca. Cement dobrej jakości jest tylko wtedy, gdy spełniono warunki proporcji wody do cementu
# do piachu w stosunku 5:2:3.