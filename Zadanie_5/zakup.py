import sys
from action import Account

file_path = sys.argv[1]
ident = str(sys.argv[2])
price = int(sys.argv[3])
quantity = sys.argv[4]

konto = Account(file_path)
if konto.import_db():
    if konto.sprzedaz(ident, price, quantity):
        konto.przeglad()
        konto.update_db()
