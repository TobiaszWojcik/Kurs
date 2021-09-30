# 2. Masz do dyspozycji generator liczb losowych,
# który wywołujemy za pomocą funkcji random() w ten sposób:
# liczba_losowa = random().
# [Na górze pliku .py trzeba wstawić linijkę from random import random,
# dlaczego tak, porozmawiamy na następnych zajęciach].
# Funkcja random generuje losowe liczby z przedziału od 0 do 1.
# Przygotuj program, który będzie losował liczbę za pomocą random() i na jej podstawie generował
# liczbę z przedziału podanego przez użytkownika
# (użytkownik podaje dolną i górną granicę zakresu,
# interesują nas tylko liczby całkowite,
# losowość nie ma znaczenia dopóki użyliśmy funkcji random do generowania liczby)
# , po czym użytkownik będzie mógł zgadywać,
# jaka liczba została wylosowana, jeżeli użytkownik poda złą liczbę,
# to program zasugeruje, czy podana liczba jest mniejsza,
# czy większa od wylosowanej. Zaprogramuj wyjście awaryjne z programu,
# jeżeli użytkownik wpisze zamiast liczby słowo EXIT.
print("Podaj 2 dowolne liczby całkowite, a następnie ja wylosuję cyfrę pomiędzy nimi, a ty ją będziesz mógł zgadnąć")
from random import random
while True:
    try:
        pierwsza_liczba = int(input("Podaj pierwszą liczbę całkowitą:"))
        break
    except:
        print("Podana wartość nie jest liczbą całkowitą sprubuj jeszcze raz!")
while True:
    try:
        liczba = int(input("Podaj pierwszą liczbę całkowitą:"))
        if liczba > pierwsza_liczba:
            druga_liczba = liczba
        else:
            druga_liczba = pierwsza_liczba
            pierwsza_liczba = liczba
        break
    except:
        print("Podana wartość nie jest liczbą całkowitą sprubuj jeszcze raz!")
print("Zgadnij jaką cyfrę wylosowałem!!")
status = True
los = round((random()*(druga_liczba-pierwsza_liczba))+pierwsza_liczba,0)
while status:
    # Zakładam że użytkownik nie będzie już popełniał błędów i nie będzie wysypywał programu
    liczba = input("Podaj swoją liczbę lub wpisz \"EXIT\" aby zrezygnować i naciśnij klawisz <enter>")
    if liczba == "EXIT":
        ("Szkoda że się poddałeś!")
        break
    liczba = int(liczba)
    if liczba > los:
        print("Podana liczba jest więsza niż moja, spróbuj ponownie")
    elif liczba < los:
        print("Podana liczba jest mniejsza niż moja, spróbuj ponownie")
    else:
        status = False
else:
    print("Brawo Zgadłeś")