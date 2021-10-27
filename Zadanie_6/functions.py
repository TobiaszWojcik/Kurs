import csv
import os


def csv_print(file, spacer=", "):
    for row in file:
        print(spacer.join(row))


def swipe_content(content, changes):
    for change in changes:
        content[int(change[0])][int(change[1])] = change[2]
    return content


class FileHandler:
    def __init__(self):
        self.path_in = None
        self.path_out = None

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
            print("Brak pliku źródłowego")
            return False

    def savefile(self, content, path_out=None):
        if path_out is None:
            path_out = self.path_in
        self.path_out = path_out
        with open(self.path_out, 'w') as file:
            csv.writer(file).writerows(content)
