import csv
import os
import json
import pickle
import pprint


# Funkcja rekurencyjna sprawdza w dół ostatni istniejący folder i zwraca jego pozycję.
# Parametr create decyduje czy funkcja tworzy podfoldery aż do pierwotnie podanej lokalizacji
def check_dir_exist(path, create=False):
    pathabs = os.path.abspath(path)
    if not os.path.isdir(pathabs):
        dip = check_dir_exist(os.path.split(path)[0], create)
        if create:
            if not os.path.split(path)[1] == "":
                os.mkdir(path)
        return dip

    return pathabs


# Funkcja drukująca zawartość listy
def csv_print(file, spacer=", "):
    for row in file:
        print(spacer.join(row))


# Funkcja zmieniająca zawartość kolumny w liście
def swipe_content(content, changes):
    max_row = len(content)
    max_col = len(content[0])
    for change in changes:
        if max_row > int(change[0]) and max_col > int(change[1]):
            content[int(change[0])][int(change[1])] = change[2]
        else:
            print("Brak możliwość zmiany komurki {}x{} na wartość:{}".format(change[0], change[1], change[2]))
    return content


# Klasa obsługująca wczytywanie oraz zapis pliku csv
class FileHandler:
    def __init__(self):
        self.path_in = ""
        self.path_out = ""
        self.filename_in = ""
        self.filename_out = ""

    # Metoda odczytu pliku csv, zwraca listę lub False w przypadku braku pliku
    def loadfile(self, path_in):
        self.path_in = path_in
        self.filename_in = os.path.basename(path_in)
        content = []
        if os.path.exists(self.path_in):
            file_extensions = self.filename_in.split('.')[-1]
            open_mode = "rb" if file_extensions == "pickle" else "r"
            with open(self.path_in, open_mode) as file:
                if file_extensions == 'csv':
                    temp = csv.reader(file, skipinitialspace=True)
                    for row in temp:
                        content.append(row)
                elif file_extensions == 'pickle':
                    content = pickle.load(file)
                elif file_extensions == 'json':
                    temp = json.load(file)
                    for kol in temp.get(list(temp.keys())[0]):
                        content.append(kol)
            return content
        else:
            print('Brak pliku o podanej nazwie: "{}"'.format(self.path_in))

            return False

    # Metoda zapisu pliku
    def savefile(self, content, path_out=None):
        self.path_out = os.path.dirname(path_out)
        self.filename_out = os.path.basename(path_out)
        check_dir_exist(self.path_out, True)
        final_dir = os.path.join(self.path_out, self.filename_out)
        file_extension = self.filename_out.split(".")[-1]
        open_mode = "wb" if file_extension == "pickle" else "w"
        with open(final_dir, open_mode) as file:
            if file_extension == "csv":
                csv.writer(file).writerows(content)
            elif file_extension == "pickle":
                pickle.dump(content, file)
            elif file_extension == "json":
                save = {'value': content}
                json.dump(save, file)
