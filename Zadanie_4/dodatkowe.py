import random
import time


# Zadanie_1

print("Zadanie 1 - Napisz proram, który wybierze największy element listy")
input("Naciśnij <Enter> aby kontynuować.")

lista_a = []
for idx in range(20):
    random_value = random.randint(0, 200)
    lista_a.append(random_value)
print(lista_a)

max = 0
for value in lista_a:
    if value > max:
        max = value
print("Największa wartość w tej liście to: {}".format(max))
print()
time.sleep(3)


# Zadanie_2

print("""Zadanie 2 - Napisz program, który policzy liczbę stringów przekazanych w liście,
        które są długości co najmniej 2 i mają taką samą pierwszą i ostatnią literę.""")
input("Naciśnij <Enter> aby kontynuować.")

lista_b = [
        "to", 1, "jest", 8, True, "nie", "bbb",
        "jest", 4, "aa", "string", False, "dd",
        None, "False", 'kot', "kajak", "zzzz"]

count_string = 0

for value in lista_b:
    if isinstance(value, str):
        if len(value) > 2:
            if value[0] == value[-1]:
                 count_string += 1

print("W tej liście:\n{lista}\njest {liczba} stringów dłuższych od 2 i o takiej\
        samej pierwszej i ostatniej literze".format(
        lista=lista_b, liczba=count_string))


# Zadanie_3

print("Zadanie 3 - Napisz program, który posortuje podaną listę (lista zawiera tylko liczby).")
input("Naciśnij <Enter> aby kontynuować.")

# Sposób 1

print("Sposób 1")
time.sleep(2)
LICZBA_LICZB = 2000
lista_c = []

for _ in range(LICZBA_LICZB):
    lista_c.append(random.randint(1, 10000))

print(lista_c)
time.sleep(2)
print("Rozpoczęcie sortowania")
# licznik = 0
lista_c_a = []
lista_c_b = []
ms = time.time()

while True:
    ostatni_element = 0
    lista_c_a.clear()
    lista_c_b.clear()

    for obecny_element in lista_c:
        if ostatni_element <= obecny_element:
            lista_c_a.append(obecny_element)
            ostatni_element = obecny_element
        else:
            lista_c_b.append(obecny_element)
    lista_c = lista_c_b + lista_c_a

    if len(lista_c_b) == 0:
        break

ms = time.time()-ms
print("Cała lista: {}".format(lista_c))
print("Czas sortowania to {} secundy.".format(ms))
time.sleep(3)


# Sposób 2

print("Sposób 2")
input("Naciśnij <Enter> aby kontynuować.")
lista_c.clear()

for _ in range(LICZBA_LICZB):
    lista_c.append(random.randint(1, 10000))

print(lista_c)
ms = time.time()
najmniejsza = [999999, 0]
time.sleep(2)
print("Rozpoczęcie sortowania")

for idx in range(LICZBA_LICZB):

    for liczba in range(LICZBA_LICZB-idx):
        if lista_c[liczba] <= najmniejsza[0]:
            najmniejsza[0] = lista_c[liczba]
            najmniejsza[1] = liczba

    lista_c.append(lista_c.pop(najmniejsza[1]))
    najmniejsza[0] = lista_c[0]

ms = time.time()-ms
print("Cała lista: {}".format(lista_c))
print("Czas sortowania to {} sekundy.".format(ms))
time.sleep(3)


# Sposób 3

print("Sposób 3")
input("Naciśnij <Enter> aby kontynuować.")
lista_c.clear()

for _ in range(LICZBA_LICZB):
    lista_c.append(random.randint(1, 10000))

print(lista_c)
time.sleep(2)
print("Rozpoczęcie sortowania")
ms = time.time()
lista_c.sort()
ms = time.time()-ms
print("Cała lista: {}".format(lista_c))
print("Czas sortowania to {} sekundy.".format(ms))
time.sleep(3)


# Zadanie_4

print("Zadanie 4 - Napisz program, który z dwóch list A i B wypisze elementy, które występują w obu listach.")
input("Naciśnij <Enter> aby kontynuować.")

lista_d = ["string", "aloha", "dd", None, "False", 'miś',
           "kajak", "jeż", "to", 1, "nic", 8, True, "nie",
           "bbb", "jest", 4, "cccc", ]
print("Lista A: {}".format(lista_b))
print("Lista B: {}".format(lista_d))
time.sleep(2)

for element in lista_b:
    if lista_d.count(element):
        print("{}".format(element))
time.sleep(3)

# Zadanie_5

print("Zadanie 5 -  Napisz program, który wypisze losowy element z listy.")
input("Naciśnij <Enter> aby kontynuować.")

print("Lista: {}".format(lista_b))
time.sleep(2)

random_value = random.randint(0, len(lista_b))
print("Wylosowany element to: '{}'".format(lista_b[random_value]))
time.sleep(3)


# Zadanie_6

print("Zadanie 6 - Napisz program, który odwróci i połączy ze sobą dwie listy A i B.")
input("Naciśnij <Enter> aby kontynuować.")

print("Lista A: {}".format(lista_b))
print("Lista B: {}".format(lista_d))
time.sleep(2)

lista_b.reverse()
lista_d.reverse()
print("Lista A`: {}".format(lista_b))
print("Lista B`: {}".format(lista_d))
time.sleep(2)

lista_marge = lista_b+lista_d
print("Połączone listy A i B: {}".format(lista_marge))
