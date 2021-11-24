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

        @manager.assign('konto')
        def account():
            print(acc.saldo_kwota)

        manager.execute('konto')

    except FileNotFoundError:
        manager.execute_param('error', "Nie udało się załadować pliku")
        break

    break

manager.execute('show_error')
