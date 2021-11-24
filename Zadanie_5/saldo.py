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

        @manager.assign('saldo')
        def pozycje():
            acc.saldo(int(sys.argv[2]), sys.argv[3])

        manager.execute('saldo')

    except FileNotFoundError:
        manager.execute_param('error', "Nie udało się załadować pliku")
        break
    acc.update_db()
    break

manager.execute('show_error')


# Old

# import sys
# from action import Account
#
# file_path = sys.argv[1]
# value = int(sys.argv[2])
# comment = sys.argv[3]
#
# konto = Account(file_path)
# if konto.import_db():
#     if konto.saldo(value, comment):
#         konto.przeglad()
#         konto.update_db()
