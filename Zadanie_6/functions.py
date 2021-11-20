import csv
import os
import json
import pickle


class ListHendler:
    def __init__(self, content):
        self.content = content

    def print_list(self, spacer=", "):
        for row in self.content:
            print(spacer.join(row))

    def swipe_content(self, changes):
        max_row = len(self.content)
        max_col = len(self.content[0])
        for change in changes:
            if len(change)>2:
                if max_row > int(change[0]) and max_col > int(change[1]):
                    self.content[int(change[0])][int(change[1])] = change[2]
                else:
                    print("Brak możliwość zmiany komurki {}x{} na wartość:{}".format(change[0], change[1], change[2]))
            else:
                print("Nie podano wszystkich parametrów do zmiany")
        return self.content


class FileHandler:
    def __init__(self, open_mode=""):
        self.open_mode = open_mode

    def loadfile(self, path):
        open_mode = 'r' + str(self.open_mode)
        with open(path, open_mode) as file:
            content = self.file_loader(file)
        return content

    def savefile(self, path, content):
        open_mode = 'w'+str(self.open_mode)
        with open(path, open_mode) as file:
            self.file_saver(file, content)


class CsvHandler(FileHandler):
    def file_saver(self, file, content):
        csv.writer(file).writerows(content)

    def file_loader(self, file):
        temp = csv.reader(file, skipinitialspace=True)
        content = []
        for row in temp:
            content.append(row)
        return content


class JSONHandler(FileHandler):
    def file_saver(self, file, content):
        json.dump(content, file)

    def file_loader(self, file):
        content = json.load(file)
        return content


class PickleHandler(FileHandler):
    def __init__(self):
        super().__init__('b')

    def file_saver(self, file, content):
        pickle.dump(content, file)

    def file_loader(self, file):
        content = pickle.load(file)
        return content

class File_Check:
    def __init__(self, path_to_check):
        self.path = path_to_check
        self.path_dir = os.path.dirname(path_to_check)
        self.filename = os.path.basename(path_to_check)
        self.file_extensions = self.filename.split(".")[-1]

    def __repr__(self):
        return self.path

    def dir_exist(self, path, create=False):
        pathabs = os.path.abspath(path)
        if not os.path.isdir(pathabs):
            dip = self.dir_exist(os.path.split(path)[0], create)
            if create:
                if not os.path.split(path)[1] == "":
                    os.mkdir(path)
            return dip

    def file_exist(self):
        return os.path.exists(self.path)

