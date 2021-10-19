class Account:
    def __init__(self, path):
        self.path = path
        self.saldo_kwota = 0
        self.zapis_zdarzen = []
        self.stan_magazynowy = {}
        self.action = []

    def zapis_akcji(self, akcja, parametry):
        self.zapis_zdarzen.append({'akcja': akcja, 'parametry': tuple(parametry)})

    def dzialanie_magazyn(self, identyfikator, liczba_sztuk):
        if identyfikator in self.stan_magazynowy:
            self.stan_magazynowy[identyfikator] = self.stan_magazynowy.get(identyfikator) + liczba_sztuk
        else:
            self.stan_magazynowy[identyfikator] = liczba_sztuk

        if self.stan_magazynowy.get(identyfikator) < 0:
            print("Brak wystarczającej ilości produktu {} w magazynie".format(identyfikator))
            return False
        return True

    def saldo(self, wartosc, komentarz="Brak komentarza"):
        if self.saldo_kwota + wartosc >= 0:
            self.saldo_kwota += wartosc
            self.zapis_akcji("saldo", [wartosc, komentarz])
        else:
            print('Brak wystarczających środków na koncie')

    def zakup(self, identyfikator, wartosc_jednostkowa, liczba_sztuk):
        if wartosc_jednostkowa > 0 < liczba_sztuk:
            if (self.saldo_kwota - (wartosc_jednostkowa * liczba_sztuk)) > 0:
                self.dzialanie_magazyn(identyfikator, liczba_sztuk)
                self.saldo_kwota -= (wartosc_jednostkowa * liczba_sztuk)
                self.zapis_akcji("zakup", [identyfikator, wartosc_jednostkowa, liczba_sztuk])
            else:
                print('Brak wystarczających środków na koncie')
        else:
            print('Błąd wprowadzonych danych')

    def sprzedaz(self, identyfikator, wartosc_jednostkowa, liczba_sztuk):
        if wartosc_jednostkowa > 0 < liczba_sztuk:
            if self.dzialanie_magazyn(identyfikator, liczba_sztuk * (-1)):
                self.saldo_kwota -= (wartosc_jednostkowa * liczba_sztuk)
                self.zapis_akcji("sprzedaz", [identyfikator, wartosc_jednostkowa, liczba_sztuk])
        else:
            print('Błąd wprowadzonych danych')

    def import_db(self, tryb='r'):
        with open(path, tryb) as file:
            status = True
            while status:
                act = file.readline()
                act = act.strip()

                if act == "saldo":
                    wartosc = int(file.readline())
                    komentarz = file.readline()
                    self.saldo(wartosc, komentarz)

                elif act == "sprzedaż" or act == "zakup":
                    identyfikator = file.readline()
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
    #
    #                 elif action_end[0] == "konto":
    #                     print("Obecny stan konta to {} groszy".format(saldo_kwota))
    #                     break
    #                 elif action_end[0] == "magazyn":
    #
    #                     for idx, produkt in enumerate(action_end[1:]):
    #                         print("{}. {} sztuk {}".format(idx + 1, produkt, stan_magazynowy.get(produkt)))
    #                     break
    #                 elif action_end[0] == "sprzedaż" or action_end[0] == "zakup":
    #                     identyfikator = action_end.pop(1)
    #                     wartosc_jednostkowa = int(action_end.pop(1))
    #                     if wartosc_jednostkowa < 0:
    #                         print("Podana wartość jednostkowa jest mniejsza od zera")
    #                     liczba_sztuk = int(action_end.pop(1))
    #                     if liczba_sztuk < 0:
    #                         print("Podana liczba sztuk jest mniejsza od zera")
    #                     if act == "sprzedaż":
    #                         sprzedaz(identyfikator, wartosc_jednostkowa, liczba_sztuk)
    #                     else:
    #                         zakup(identyfikator, wartosc_jednostkowa, liczba_sztuk)
    #                     for a in zapis_zdarzen:
    #                         for b in a.values():
    #                             if type(b) is tuple:
    #                                 for c in b:
    #                                     print(c)
    #                             else:
    #                                 print(b)
    #                     print("stop")
    #                 elif action_end[0] == "przegląd":
    #                     for a in zapis_zdarzen[int(action_end[1]): int(action_end[2]) + 1]:
    #                         for b in a.values():
    #                             if type(b) is tuple:
    #                                 for c in b:
    #                                     print(c)
    #                             else:
    #                                 print(b)
    #                     print("stop")
    #                 else:
    #                     break
    #                 pass
    #             else:
    #                 status = False
    #
    #             if len(action) >= 2:
    #                 del action[0]
    #                 act = action[0]
    #             else:
    #                 act = ""
    #         else:
    #             if (act) == "":
    #                 pass
    #             else:
    #                 print("Niedozwolona akcja !!")
    #
    #         while
    #         if file.readline() == 'saldo':
    #             pass
    #         elif file.readline() ==
    #
    #
    #
    # while True:
    #     command = input()
    #     action.append(command)
    #     if command == "stop":
    #         break
    # if len(action):
    #     act = action[0]
    # else:
    #     act = ""
    # status = True
    # while status:
    #     act = act.strip()
    #     if act == "saldo":
    #         wartosc = int(action.pop(1))
    #         test(wartosc)
    #         komentarz = action.pop(1)
    #         test(komentarz)
    #         saldo(wartosc, komentarz)
    #     elif act == "sprzedaż" or act == "zakup":
    #         identyfikator = action.pop(1)
    #         wartosc_jednostkowa = int(action.pop(1))
    #         if wartosc_jednostkowa < 0:
    #             print("Podana wartość jednostkowa jest mniejsza od zera")
    #         liczba_sztuk = int(action.pop(1))
    #         if liczba_sztuk < 0:
    #             print("Podana liczba sztuk jest mniejsza od zera")
    #         if act == "sprzedaż":
    #             sprzedaz(identyfikator, wartosc_jednostkowa, liczba_sztuk)
    #         else:
    #             zakup(identyfikator, wartosc_jednostkowa, liczba_sztuk)
    #     elif act == "stop":
    #         if action_end[0] == "saldo":
    #             if len(action_end) == 1:
    #                 print(saldo_kwota)
    #             else:
    #                 wartosc = int(action_end.pop(1))
    #                 test(wartosc)
    #                 komentarz = action_end.pop(1)
    #                 test(komentarz)
    #                 saldo(wartosc, komentarz)
    #         elif action_end[0] == "konto":
    #             print("Obecny stan konta to {} groszy".format(saldo_kwota))
    #             break
    #         elif action_end[0] == "magazyn":
    #
    #             for idx, produkt in enumerate(action_end[1:]):
    #                 print("{}. {} sztuk {}".format(idx+1, produkt, stan_magazynowy.get(produkt)))
    #             break
    #         elif action_end[0] == "sprzedaż" or action_end[0]== "zakup":
    #             identyfikator = action_end.pop(1)
    #             wartosc_jednostkowa = int(action_end.pop(1))
    #             if wartosc_jednostkowa < 0:
    #                 print("Podana wartość jednostkowa jest mniejsza od zera")
    #             liczba_sztuk = int(action_end.pop(1))
    #             if liczba_sztuk < 0:
    #                 print("Podana liczba sztuk jest mniejsza od zera")
    #             if act == "sprzedaż":
    #                 sprzedaz(identyfikator, wartosc_jednostkowa, liczba_sztuk)
    #             else:
    #                 zakup(identyfikator, wartosc_jednostkowa, liczba_sztuk)
    #             for a in zapis_zdarzen:
    #                 for b in a.values():
    #                     if type(b) is tuple:
    #                         for c in b:
    #                             print(c)
    #                     else:
    #                         print(b)
    #             print("stop")
    #         elif action_end[0] == "przegląd":
    #             for a in zapis_zdarzen [int(action_end[1]): int(action_end[2])+1  ]:
    #                 for b in a.values():
    #                     if type(b) is tuple:
    #                         for c in b:
    #                             print(c)
    #                     else:
    #                         print(b)
    #             print("stop")
    #         else:
    #             break
    #         pass
    #     else:
    #         status = False
    #
    #     if len(action) >= 2:
    #         del action[0]
    #         act = action[0]
    #     else:
    #         act = ""
    # else:
    #     if(act) == "":
    #         pass
    #     else:
    #         print("Niedozwolona akcja !!")
    #
