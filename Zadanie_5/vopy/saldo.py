import sys
from action import Account

file_path = sys.argv[1]
value = int(sys.argv[2])
comment = sys.argv[3]

konto = Account(file_path)
if konto.import_db():
    if konto.saldo(value, comment):
        konto.przeglad()
        konto.update_db()

# Pusty komentarz aby odsiwrzyć pliki
print()