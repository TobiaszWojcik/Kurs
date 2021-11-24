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

        @manager.assign('zakup')

        def pozycje():
            acc.zakup(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))

        manager.execute('zakup')

        @manager.assign('przeglad')
        def przeglad(start_stop=[0, 0]):
            acc.przeglad(start_stop[0], start_stop[1])

        manager.execute('przeglad')
    except FileNotFoundError:
        manager.execute_param('error', "Nie udało się załadować pliku")
        break
    acc.update_db()
    break

manager.execute('show_error')

# Old
#
# import sys
# from action import Account
#
# file_path = sys.argv[1]
# ident = str(sys.argv[2])
# price = int(sys.argv[3])
# quantity = int(sys.argv[4])
#
# konto = Account(file_path)
# if konto.import_db():
#     if konto.zakup(ident, price, quantity):
#         konto.przeglad()
#         konto.update_db()
