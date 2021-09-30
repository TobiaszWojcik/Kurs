<<<<<<< HEAD
import sys
liczba_paczek_wyslanych = 0
liczba_kilogramow_wyslanych = 0
liczba_elementow = 0
liczba_paczek_oversize = 0
liczba_paczek_undersize = 0
liczba_paczek_bez_wagi = 0
min_numer_paczki = 0
min_paczka = 20
max_element = 10
min_element = 1
max_paczka = 20
formulka = """
Liczba paczek wysłanych: {} sztuk.
Liczba kilogramów wysłanych: {} kg.
Suma 'pustych' kilogramów: {} kg.
Paczka nr: {} miała najwięcej pustych kilogramów ({} kg).
Wyslano {} elementów."""
obecna_paczka = 0
string_oversize = "<Błąd> Waga elementu nr:{} przekracza dopuszczalną wagę {} kg i wynosi {} kg"
string_undersize = "<Błąd> Waga elementu nr:{} jest mniejsza niż minimum {}kg i wynosi {}kg"
string_nosize = "<Błąd> Waga elementu nr:{} nie została podana, sprawdź w systemie!!"


print("""Wybierz sposób wprowadzania danych:
Wprowadzanie z pliku elementy.txt - \"e\"
Wprowadzanie ręczne - \"r\" """)
status_input = True
while(True):
    status = input("Wybierz sposób i naciśnij <ENTER>")
    if (status_input):
        try:
            kolejny_element = float(status)
            status = 1
            break
        except:
            status_input = False

    if status == "r":
        status = 2
        break
    elif status == "e":
        status = 3
        break
    print ("Podano niepoprawną komendę")
if status == 3:
    try:
        source = open("elementy.txt")
        for kolejny_element in source:
            liczba_elementow += 1
            kolejny_element = float(kolejny_element.replace(",",".",1))
    # Sprawdzenie warunków wysyłki elementów
            if kolejny_element == 0:
                print("Paczka o masie 0 kg. Zakończenie pakowania")
                break
                # liczba_paczek_bez_wagi += 1
                # print(string_nosize.format(liczba_elementow))
            elif kolejny_element > 10:
                liczba_paczek_oversize += 1
                print(string_oversize.format(liczba_elementow, max_element, kolejny_element))
            elif kolejny_element < 1:
                liczba_paczek_undersize += 1
                print(string_undersize.format(liczba_elementow, min_element, kolejny_element))

    # Pierwsza paczka
            if liczba_paczek_wyslanych == 0:
                liczba_paczek_wyslanych += 1

    # Sumowanie kilogramów
            liczba_kilogramow_wyslanych += kolejny_element

    # Pakowanie do paczek max
            if (obecna_paczka+kolejny_element) <= max_paczka:
                obecna_paczka += kolejny_element

            else:
                # Podaje wagę wszystkich paczek
                # print("{}. {}kg".format(liczba_paczek_wyslanych, obecna_paczka))
                if obecna_paczka < min_paczka:
                    min_paczka = obecna_paczka
                    min_numer_paczki = liczba_paczek_wyslanych
                liczba_paczek_wyslanych += 1
                obecna_paczka = kolejny_element
        source.close()
        if obecna_paczka < min_paczka:
            min_paczka = obecna_paczka
            min_numer_paczki = liczba_paczek_wyslanych
        puste = 20*liczba_paczek_wyslanych-liczba_kilogramow_wyslanych
        zle_paczki = liczba_paczek_bez_wagi + liczba_paczek_undersize + liczba_paczek_oversize
        print(formulka.format(liczba_paczek_wyslanych, liczba_kilogramow_wyslanych, puste, min_numer_paczki, 20 - min_paczka, liczba_elementow))

    except:
        print("Błąd wprowadzania danych!! Upewni się że plik z danymi jest dostępny")
        print("Możesz wygenerować plik liczb losowy wpisując \"python3 generator_elementow.py\"")
if status == 2:
    pass
=======
# Program do obsługi ladowarki paczek

liczba_paczek_wyslanych = 0
liczba_kilogramow_wyslanych = 0
liczba_elementow = 0
liczba_paczek_oversize=0
liczba_paczek_undersize=0
Liczba_paczek_bez_wagi=0
paczka_z_najwiekszym_brakiem = 0
min_numer_paczki=0
min_paczka = 0
max_element = 10
min_element = 1
max_paczka = 20

obecna_paczka = 0
source = open("elementy.txt")
for kolejny_element in source:
    liczba_elementow += 1
    kolejny_element=float(kolejny_element)
    if kolejny_element>10:
        print("<Błąd> Waga elementu nr:{} przekracza dopuszczalną wagę {} kg i wynosi {} kg".format(liczba_elementow, max_element,kolejny_element))
    elif kolejny_element<1 and kolejny_element>0:
        print("<Błąd> Waga elementu nr:{} jest mniejsza niż minimum {}kg i wynosi {}kg".format(liczba_elementow, min_element, kolejny_element))
    elif kolejny_element==0:
        print("<Błąd> Waga elementu nr:{} nie została podana, sprawdź w systemie!!".format(liczba_elementow))

    if(liczba_paczek_wyslanych==0):liczba_paczek_wyslanych+=1
    liczba_kilogramow_wyslanych+=kolejny_element
    if (obecna_paczka+kolejny_element)<=max_paczka:
        obecna_paczka +=kolejny_element
    else:
        if obecna_paczka<min_paczka:
            min_paczka = obecna_paczka
            min_numer_paczki = liczba_paczek_wyslanych
        liczba_paczek_wyslanych=+1
        obecna_paczka = kolejny_element
source.close()
#else:
#   liczba_paczek_wyslanych=+1
>>>>>>> parent of ad396ee... Dodanie wydruku wyników pakowania, poprawa generatowa elementów losowych
