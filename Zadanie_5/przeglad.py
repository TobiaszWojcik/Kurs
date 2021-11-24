import sys
from action import Account
from action import Manager

manager = Manager()
acc = Account()


@manager.assign("error")
def get_error(take_error):
    manager.error = take_error


@manager.assign('show_error')
def show_err():
    if manager.error:
        print(manager.error)


while True:
    try:
        acc.get_file_path(sys.argv[1])
    except IndexError:
        manager.execute_param('error', 'Brak ścieżki wejścia')
        break
    try:
        acc.import_db()

        @manager.assign('przeglad_rama')
        def param():
            if len(sys.argv) == 4:
                return int(sys.argv[2]), int(sys.argv[3])
            elif len(sys.argv) == 3:
                return int(sys.argv[2]), 0
            else:
                return [0, 0]

        @manager.assign('przeglad')
        def przeglad(start_stop=[0, 0]):
            acc.przeglad(start_stop[0], start_stop[1])

        manager.execute_param('przeglad', manager.execute('przeglad_rama'))

    except FileNotFoundError:
        manager.execute_param('error', "Nie udało się załadować pliku")
        break

    break

manager.execute('show_error')

# OLD
#
# import sys
# from action import Account
#
# file_path = sys.argv[1]
#
# konto = Account()
# konto.get_file_path(file_path)
# if konto.import_db():
#     konto.przeglad()
