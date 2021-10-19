import sys
from action import Account

file_path = sys.argv[1]

konto = Account(file_path)
if konto.import_db():
    print(konto.saldo_kwota)
