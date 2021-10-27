import csv
import os



class FileHandler:
    def __init__(self, path_in, path_out=None):
        if os.path.exists(path_in):
            self.path_in = path_in
            if path_out is None:
                path_out = path_in
            self.path_out = path_out
        else:
            print("Brak pliku źródłowego")

    def loadfile(self):
        content = []
        with open(self.path_in, 'r') as file:
            temp = csv.reader(file)
            for row in temp:
                content.append(row)
        return content



openfile = FileHandler('snakes_count_100.csv')
print(openfile.loadfile())
