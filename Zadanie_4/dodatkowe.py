import random
import time
"""
1. Napisz proram, który wybierze największy element listy
2. Napisz program, który policzy liczbę stringów przekazanych w liście,
które są długości co najmniej 2 i mają taką samą pierwszą i ostatnią literę.
3. Napisz program, który posortuje podaną listę (lista zawiera tylko liczby).
4. Napisz program, który z dwóch list A i B wypisze elementy, które występują w obu listach.
5. Napisz program, który wypisze losowy element z listy.
6. Napisz program, który odwróci i połączy ze sobą dwie listy A i B.
"""
# # Zadanie_1
# lista_a = []
# for idx in range(20):
#     random_value = random.randint(0, 200)
#     lista_a.append(random_value)
# print(lista_a)
# max = 0
# for value in lista_a:
#     if value > max:
#         max = value
# print("Największa wartość w tej liście to: {}".format(max))
# print()
# # Zadanie_2
# lista_b = [
#         "to", 1, "jest", 8, True, "nie", "bbb",
#         "jest", 4, "aa", "string", False, "dd",
#         None, "False", 'kot', "kajak", "zzzz"]
# count_string = 0
# for value in lista_b:
#     if isinstance(value, str):
#         if len(value) > 2:
#             if value[0] == value[-1]:
#                  count_string += 1
# print("W tej liście:\n{lista}\njest {liczba} stringów dłuższych od 2 i o takiej\
#         samej pierwszej i ostatniej literze".format(
#         lista=lista_b, liczba=count_string))

# Zadanie_3
#
# Sposób 1
LICZBA_LICZB = 2000

lista_c = []
for _ in range(LICZBA_LICZB):
    lista_c.append(random.randint(1, 10000))
print(lista_c)
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
time.sleep(5)


# Sposób 2

lista_c.clear()
for _ in range(LICZBA_LICZB):
    lista_c.append(random.randint(1, 10000))
print(lista_c)
ms = time.time()
najmniejsza = [999999, 0]
for idx in range(LICZBA_LICZB):
    for liczba in range(LICZBA_LICZB-idx):
        if lista_c[liczba] <= najmniejsza[0]:
            najmniejsza[0] = lista_c[liczba]
            najmniejsza[1] = liczba
    lista_c.append(lista_c.pop(najmniejsza[1]))
    najmniejsza[0] = lista_c[0]
ms = time.time()-ms
print("Cała lista: {}".format(lista_c))
print("Czas sortowania to {} secundy.".format(ms))
