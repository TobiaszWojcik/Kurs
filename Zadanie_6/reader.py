import sys
import os
from functions import FileHandler
from functions import csv_print
from functions import swipe_content
from functions import check_dir_exist


path_in = sys.argv[1]
if os.path.isfile(path_in):
    path_out = sys.argv[2]
    changes = []
    dirout = check_dir_exist(path_out, True)
    for change in sys.argv[3:]:
        changes.append(change.split(","))
    openfile = FileHandler()
    content = (openfile.loadfile(path_in))

    if content:
        content = swipe_content(content, changes)
        csv_print(content)
        openfile.savefile(content, path_out)
else:
    if os.path.isdir(path_in):
        print(os.listdir(path_in))
    else:
        print(os.listdir(check_dir_exist(path_in)))
