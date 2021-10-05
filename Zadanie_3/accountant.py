import sys
saldo_kwota = 0
zapis_zdarzen = []
action = sys.argv[1:]
action_cp = tuple(action)
is_test = False


stan_magazynowy = {} # identyfikator: liczba_sztuk

def dzialanie_magazyn(identyfikator, liczba_sztuk):
    if stan_magazynowy.get(identyfikator) == None:
        stan_magazynowy[identyfikator]=liczba_sztuk
    else:
        stan_magazynowy.update(identyfikator = stan_magazynowy.get(identyfikator)+liczba_sztuk)
    if (stan_magazynowy.get(identyfikator)-liczba_sztuk<0):
            print("Brak wystarczającej ilości produktu {} w magazynie".format(identyfikator))

def zapis_akcji(akcja, parametry):
    zapis_zdarzen.append({'akcja': akcja,'parametry': (parametry) })

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
        if action == "sprzedaż":
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
        pass
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
print (action_cp)
print (saldo_kwota)
print (stan_magazynowy)