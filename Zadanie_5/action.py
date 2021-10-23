class Account:
    def __init__(self, path):
        self.FILE_PATH = path
        self.saldo_kwota = 0
        self.zapis_zdarzen = []
        self.stan_magazynowy = {}

    def zapis_akcji(self, akcja, parametry):
        self.zapis_zdarzen.append({'akcja': akcja, 'parametry': tuple(parametry)})

    def dzialanie_magazyn(self, identyfikator, liczba_sztuk):
        if liczba_sztuk < 0:
            if identyfikator in self.stan_magazynowy:
                if (self.stan_magazynowy.get(identyfikator) + liczba_sztuk) >= 0:
                    self.stan_magazynowy[identyfikator] = self.stan_magazynowy.get(identyfikator) + liczba_sztuk
                else:
                    print("Brak wystarczającej ilości produktu {} w magazynie, pozostało {} szt.".format(
                            identyfikator,
                            self.stan_magazynowy[identyfikator]))
                    return False
            else:
                print("Brak takiego produktu {} w magazynie.".format(identyfikator))
                return False
        else:
            if identyfikator in self.stan_magazynowy:
                self.stan_magazynowy[identyfikator] = self.stan_magazynowy.get(identyfikator) + liczba_sztuk
            else:
                self.stan_magazynowy[identyfikator] = liczba_sztuk
        return True

    def saldo(self, wartosc, komentarz="Brak komentarza"):
        if self.saldo_kwota + wartosc >= 0:
            self.saldo_kwota += wartosc
            self.zapis_akcji("saldo", [wartosc, komentarz])
            return True
        else:
            print('Brak wystarczających środków na koncie')
            return False

    def zakup(self, identyfikator, wartosc_jednostkowa, liczba_sztuk):
        if wartosc_jednostkowa > 0 < liczba_sztuk:
            if (self.saldo_kwota - (wartosc_jednostkowa * liczba_sztuk)) > 0:
                self.dzialanie_magazyn(identyfikator, liczba_sztuk)
                self.saldo_kwota -= (wartosc_jednostkowa * liczba_sztuk)
                self.zapis_akcji("zakup", [identyfikator, wartosc_jednostkowa, liczba_sztuk])
                return True
            else:
                print('Brak wystarczających środków na koncie')
                return False
        else:
            print('Błąd wprowadzonych danych')
            return False

    def sprzedaz(self, identyfikator, wartosc_jednostkowa, liczba_sztuk):
        if wartosc_jednostkowa > 0 < liczba_sztuk:
            if self.dzialanie_magazyn(identyfikator, liczba_sztuk * (-1)):
                self.saldo_kwota += (wartosc_jednostkowa * liczba_sztuk)
                self.zapis_akcji("sprzedaż", [identyfikator, wartosc_jednostkowa, liczba_sztuk])
                return True
            else:
                return False
        else:
            print('Błąd wprowadzonych danych')
            return False

    def import_db(self, tryb='r'):
        with open(self.FILE_PATH, tryb) as file:
            status = True
            while status:
                act = file.readline()
                act = act.strip()

                if act == "saldo":
                    wartosc = int(file.readline())
                    komentarz = file.readline().rstrip()
                    self.saldo(wartosc, komentarz)

                elif act == "sprzedaż" or act == "zakup":
                    identyfikator = file.readline().rstrip()
                    wartosc_jednostkowa = int(file.readline())
                    liczba_sztuk = int(file.readline())
                    if act == "sprzedaż":
                        self.sprzedaz(identyfikator, wartosc_jednostkowa, liczba_sztuk)
                    else:
                        self.zakup(identyfikator, wartosc_jednostkowa, liczba_sztuk)

                elif act == "stop":
                    break

                else:
                    status = False
            else:
                print('Błąd wprowadzania danych')
                return False
        return True

    def przeglad(self):
        for line in self.zapis_zdarzen:
            for b in line.values():
                if type(b) is tuple:
                    for c in b:
                        print(c)
                else:
                    print(b)
        print("stop")

    def update_db(self):
        with open(self.FILE_PATH, 'w') as file:
            for line in self.zapis_zdarzen:
                for b in line.values():
                    if type(b) is tuple:
                        for c in b:
                            file.write(str(c)+'\n')
                    else:
                        file.write(str(b)+'\n')
            file.write(str("stop\n"))

    def magazyn(self, identyfikator):
        for produkt in identyfikator:
            if produkt in self.stan_magazynowy:
                stan = self.stan_magazynowy.get(produkt)
            else:
                stan = 0
            print("{}: {}".format(produkt, stan))
