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

        @manager.assign('magazyn_pozycje')
        def pozycje(table):
            return table


        @manager.assign('magazyn')
        def mag(pozycje):
            acc.magazyn(pozycje)

        manager.execute_param('magazyn', (manager.execute_param('magazyn_pozycje', sys.argv[2:])))

    except FileNotFoundError:
        manager.execute_param('error', "Nie udało się załadować pliku")
        break

    break

manager.execute('show_error')

# OLD
# import sys
# from action import Account
#
# file_path = sys.argv[1]
# ident = sys.argv[2:]
#
# konto = Account(file_path)
# if konto.import_db():
#     konto.magazyn(ident)
