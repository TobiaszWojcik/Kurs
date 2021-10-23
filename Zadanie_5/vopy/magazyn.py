import sys
from action import Account

file_path = sys.argv[1]
ident = sys.argv[2:]

konto = Account(file_path)
if konto.import_db():
    konto.magazyn(ident)
