import sys
saldo_kwota = 0
zapis_zdarzen = []
action_end = sys.argv[1:]
is_test = False


stan_magazynowy = {} # identyfikator: liczba_sztuk

def dzialanie_magazyn(identyfikator, liczba_sztuk):
    if stan_magazynowy.get(identyfikator) == None:
        stan_magazynowy[identyfikator] = liczba_sztuk
    else:
        stan_magazynowy[identyfikator] = stan_magazynowy.get(identyfikator)+liczba_sztuk
    if (stan_magazynowy.get(identyfikator)<0):
            print("Brak wystarczającej ilości produktu {} w magazynie".format(identyfikator))

def zapis_akcji(akcja, parametry):
    zapis_zdarzen.append({'akcja': akcja,'parametry': tuple(parametry) })

def test(tekst):
    if is_test:
        print (tekst)

def saldo (wartosc, komentarz = "Brak komentarza"):
    zapis_akcji("saldo", [wartosc, komentarz])
    global saldo_kwota
    saldo_kwota += wartosc

def zakup (identyfikator, wartosc_jednostkowa, liczba_sztuk):
    zapis_akcji("zakup",[identyfikator, wartosc_jednostkowa, liczba_sztuk])
    dzialanie_magazyn(identyfikator, liczba_sztuk)
    global saldo_kwota
    saldo_kwota -= (wartosc_jednostkowa * liczba_sztuk)
    if saldo_kwota < 0:
        print("Brak wystarczających środków")

def sprzedaz (identyfikator, wartosc_jednostkowa, liczba_sztuk):
    zapis_akcji("sprzedaz",[identyfikator, wartosc_jednostkowa, liczba_sztuk])
    dzialanie_magazyn(identyfikator, liczba_sztuk*(-1))
    global saldo_kwota
    saldo_kwota += (wartosc_jednostkowa * liczba_sztuk)

action = []

while True:
    command = input()
    action.append(command)
    if command == "stop":
        break
if len(action):
    act = action[0]
else:
    act = ""
status = True
while status:
    act = act.strip()
    if act == "saldo":
        wartosc = int(action.pop(1))
        test(wartosc)
        komentarz = action.pop(1)
        test(komentarz)
        saldo(wartosc, komentarz)
    elif act == "sprzedaż" or act == "zakup":
        identyfikator = action.pop(1)
        wartosc_jednostkowa = int(action.pop(1))
        if wartosc_jednostkowa < 0:
            print("Podana wartość jednostkowa jest mniejsza od zera")
        liczba_sztuk = int(action.pop(1))
        if liczba_sztuk < 0:
            print("Podana liczba sztuk jest mniejsza od zera")
        if act == "sprzedaż":
            sprzedaz(identyfikator, wartosc_jednostkowa, liczba_sztuk)
        else:
            zakup(identyfikator, wartosc_jednostkowa, liczba_sztuk)
    elif act == "stop":
        if action_end[0] == "saldo":
            if len(action_end) == 1:
                print(saldo_kwota)
            else:
                wartosc = int(action_end.pop(1))
                test(wartosc)
                komentarz = action_end.pop(1)
                test(komentarz)
                saldo(wartosc, komentarz)
        elif action_end[0] == "konto":
            print("Obecny stan konta to {} groszy".format(saldo_kwota))
            break
        elif action_end[0] == "magazyn":

            for idx, produkt in enumerate(action_end[1:]):
                print("{}. {} sztuk {}".format(idx+1, produkt, stan_magazynowy.get(produkt)))
            break
        elif action_end[0] == "sprzedaż" or action_end[0]== "zakup":
            identyfikator = action_end.pop(1)
            wartosc_jednostkowa = int(action_end.pop(1))
            if wartosc_jednostkowa < 0:
                print("Podana wartość jednostkowa jest mniejsza od zera")
            liczba_sztuk = int(action_end.pop(1))
            if liczba_sztuk < 0:
                print("Podana liczba sztuk jest mniejsza od zera")
            if act == "sprzedaż":
                sprzedaz(identyfikator, wartosc_jednostkowa, liczba_sztuk)
            else:
                zakup(identyfikator, wartosc_jednostkowa, liczba_sztuk)
            for a in zapis_zdarzen:
                for b in a.values():
                    if type(b) is tuple:
                        for c in b:
                            print(c)
                    else:
                        print(b)
            print("stop")
        elif action_end[0] == "przegląd":
            for a in zapis_zdarzen [int(action_end[1]): int(action_end[2])+1  ]:
                for b in a.values():
                    if type(b) is tuple:
                        for c in b:
                            print(c)
                    else:
                        print(b)
            print("stop")
        else:
            break
        pass
    else:
        status = False

    if len(action) >= 2:
        del action[0]
        act = action[0]
    else:
        act = ""
else:
    if(act) == "":
        pass
    else:
        print("Niedozwolona akcja !!")

