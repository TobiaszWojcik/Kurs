import sys
saldo_kwota = 0
zapis_zdarzen = []
action = sys.argv[1:]
action_cp = tuple(action)
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

test (action)
if len(action):
    act = action[0]
else:
    act = ""
# while action[0] == "saldo" or action[0] == "sprzedaż" or action[0] == "zakup" or action[0] == "konto" or action[0] == "magazyn" or action[0] == "przedląd" action[0] == "stop":
while act == "saldo" or act == "sprzedaż" or act == "zakup" or act == "stop":

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
    # elif action == "sprzedaż":
    #     identyfikator = action.pop(1)
    #     wartosc_jednostkowa = int(action.pop(1))
    #     if wartosc_jednostkowa < 0:
    #         print("Podana wartość jednostkowa jest mniejsza od zera")
    #     liczba_sztuk = int(action.pop(1))
    #     if liczba_sztuk < 0:
    #         print("Podana liczba sztuk jest mniejsza od zera")
    #     sprzedaz(identyfikator, wartosc_jednostkowa, liczba_sztuk)
    # elif action == "zakup":
    #     identyfikator = action.pop(1)
    #     wartosc_jednostkowa = int(action.pop(1))
    #     if wartosc_jednostkowa<0:
    #         print("Podana wartość jednostkowa jest mniejsza od zera")
    #     liczba_sztuk = int(action.pop(1))
    #     if liczba_sztuk<0:
    #         print("Podana liczba sztuk jest mniejsza od zera")
    #     zakup(identyfikator, wartosc_jednostkowa, liczba_sztuk)
    # elif action == "konto":
    #     pass
    # elif action == "magazyn":
    #     pass
    # elif action == "przedląd":
    #     pass
    elif act == "stop":
        while True:
            act = input("Podaj operację do wykonania: ")
            act = act.strip()
            if act == "saldo":
                wartosc = int(input("Podaj wartość salda: "))
                test(wartosc)
                komentarz = input("Podaj komentarz do wpisu: ")
                test(komentarz)
                saldo(wartosc, komentarz)
            elif act == "sprzedaż" or act == "zakup":
                identyfikator = input("Podaj identyfikator produktu: ")
                wartosc_jednostkowa = int(input("Podaj cenę jednostkową w groszach: "))
                if wartosc_jednostkowa < 0:
                    print("Podana wartość jednostkowa jest mniejsza od zera")
                liczba_sztuk = int(input("Podaj liczbę sztuk: "))
                if liczba_sztuk < 0:
                    print("Podana liczba sztuk jest mniejsza od zera")
                if act == "sprzedaż":
                    sprzedaz(identyfikator.strip(), wartosc_jednostkowa, liczba_sztuk)
                else:
                    zakup(identyfikator.strip(), wartosc_jednostkowa, liczba_sztuk)
            elif act == "konto":
                print("Obecny stan konta to {} groszy".format(saldo_kwota))
                break
            elif act == "magazyn":
                produkty = input("Podaj produkty do wypisania, identyfikatory oddziel przecinkiem\",\"")
                produkty = produkty.split(",")
                for idx, produkt in enumerate(produkty):
                    produkt = produkt.strip()
                    print("{}. {} sztuk {}".format(idx+1, produkt, stan_magazynowy.get(produkt)))
                print(produkty)
                break
            elif act == "przegląd":
                test("Przegląd")
                for idx, wydazenie in enumerate(zapis_zdarzen):
                    print("{}. {}".format(idx+1, wydazenie))
            else:
                break
    del action[0]
    if len(action):
        act = action[0]
    else:
        act = ""
else:
    if(act) == "":
        pass
    else:
        print("Niedozwolona akcja !!")
test(action_cp)
test(saldo_kwota)
test(stan_magazynowy)