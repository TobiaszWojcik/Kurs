while(True):
    dlugosc_ciag = 0
    x = input("Podaj liczbę całkowitą od 1 do 100 lub wpisz 0 aby zakończyć program : ")
    if x == "0":
        break
    if x == "":
        print("Nie podałeś żadnej wartości!")
        continue
    x = int(x)
    if x > 100 and x < 1:
        print("Podałeś złą liczbę!")
        continue
    else:
        print("Ciąg Collatza dla liczby {} to: ".format(x))
        print(x)
        while x != 1:
            dlugosc_ciag += 1
            if x % 2 == 0:
                x /= 2
            else:
                x = 3 * x + 1
            print(int(x))
        else:
            print("Długość ciągu to: {} liczb".format(dlugosc_ciag+1))
            print()
            print()

