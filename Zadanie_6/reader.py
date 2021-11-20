import sys
from functions import ListHendler, CsvHandler, JSONHandler, PickleHandler, File_Check

if len(sys.argv)>2:
    path_in = File_Check(sys.argv[1])
    ext = path_in.file_extensions.lower()
    if path_in.file_exist():
        if ext == "json":
            file = JSONHandler()
        elif ext == "pickle":
            file = PickleHandler()
        elif ext == "csv":
            file = CsvHandler()
        else:
            file = False
            print(f"Nieobsługiwany format pliku (.{path_in.file_extensions})")

        if file:
            content = ListHendler(file.loadfile(str(path_in)))
            changes = []
            if len(sys.argv)>3:
                for change in sys.argv[3:]:
                    changes.append(change.split(","))
                content.swipe_content(changes)
            content.print_list()
        path_out = File_Check(sys.argv[2])
        path_out.dir_exist(path_out.path_dir, True)
        ext = path_out.file_extensions.lower()
        if ext == "json":
            file = JSONHandler()
        elif ext == "pickle":
            file = PickleHandler()
        elif ext == "csv":
            file = CsvHandler()
        else:
            file = False
            print(f"Ten plik nie może zostać zapisany")

        if file:
            file.savefile(path_out.path, content.content)
    else:
        print("Plik o podanym adresie nie istnieje")
else:
    print("Nie podano pliku źródłowego")