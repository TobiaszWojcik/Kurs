import csv
import os


# Funkcja drukująca zawartość listy
def csv_print(file, spacer=", "):
    for row in file:
        print(spacer.join(row))


# Funkcja zmieniająca zawartość kolumny w liście
def swipe_content(content, changes):
    for change in changes:
        content[int(change[0])][int(change[1])] = change[2]
    return content


# Klasa obsługująca wczytywanie oraz zapis pliku csv
class FileHandler:
    def __init__(self):
        self.path_in = None
        self.path_out = None

    # Metoda odczytu pliku csv, zwraca listę lub False w przypadku braku pliku
    def loadfile(self, path_in):
        self.path_in = path_in
        content = []
        if os.path.exists(self.path_in):
            with open(self.path_in, 'r') as file:
                temp = csv.reader(file, skipinitialspace=True)
                for row in temp:
                    content.append(row)
            return content
        else:
            print('Brak pliku o podanej nazwie: "{}"'.format(self.path_in))
            return False

    # Metoda zapisu pliku
    def savefile(self, content, path_out=None):
        if path_out is None:
            path_out = self.path_in
        self.path_out = path_out
        with open(self.path_out, 'w') as file:
            csv.writer(file).writerows(content)
