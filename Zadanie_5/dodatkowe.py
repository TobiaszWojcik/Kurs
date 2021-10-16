# Funkcje
# Stwórz funkcję, która przyjmuje dwie liczby całkowite, które są granicami przedziału
# liczbowego i zwraca informację czy w tym przedziale są liczby podzielne przez 3
# i ile jest tam takich liczb. Przykładowo func(1,7) zwróci (True, 2).

def podzielne(minim, maxim):
    ile = 0
    for sprawdz in range(minim, maxim+1):
        if sprawdz % 3 == 0:
            ile += 1
    if ile:
        return True, ile
    else:
        return False, ile


print(podzielne(1, 7))

print(podzielne(4, 5))

# Klasy
# Stwórz klasę pies, wiedząc, że pies może mieć charakterystyczne imię, rasę, kolor sierści,
# a ponadto powinien móc szczekać i wyć.


class Pies:
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


class Betoniarka:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.podlaczona = False
        self.wlacz = False
        self.wsyp = {'piach': 0,
                     'woda': 0,
                     'cement': 0}

    def on(self):
        self.wlacz = True
        if self.podlaczona:
            print("Betoniarka włączona")
            if self.wsyp['woda'] and self.wsyp['piach'] and self.wsyp['cement']:
                beton = "Beton"
                if (self.wsyp['woda'] / 5) == (self.wsyp['piach'] / 3) == (self.wsyp['cement'] / 2):
                    beton += " dobrej jakości"
                self.wsyp['woda'] = 0
                self.wsyp['piach'] = 0
                self.wsyp['cement'] = 0
                return beton

        else:
            "Betoniarka nie podłączona do prądu"

    def off(self):
        self.wlacz = False
        print("Betoniarka wyłączona")

    def fill(self, piach, woda, cement):
        self.wsyp['piach'] = piach
        self.wsyp['woda'] = woda
        self.wsyp['cement'] = cement

    def podlacz(self):
        self.podlaczona = True

    def odlacz(self):
        self.podlaczona = False


betoniarka = Betoniarka(50)
betoniarka.fill(10, 4, 6)
betoniarka.podlacz()
print(betoniarka.on())
betoniarka.fill(10, 6, 4)
print(betoniarka.on())
betoniarka.fill(6, 10, 4)
print(betoniarka.on())
