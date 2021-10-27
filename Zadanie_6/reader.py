import sys
from functions import FileHandler
from functions import csv_print
from functions import swipe_content

path_in = sys.argv[1]
path_out = sys.argv[2]
changes=[]
for change in sys.argv[3:]:
    changes.append(change.split(","))

openfile = FileHandler()
content = (openfile.loadfile(path_in))

swipe_content(content, changes)

csv_print(content)

openfile.savefile(content, path_out)
