#from bank import Bank, Customer, Account
from bank import *

bank = Bank('SGH Bank')
c1 = bank.create_customer('John', 'Brown')
a1 = bank.create_account(c1)
a2 = bank.create_account(c1, 'EUR')
c2 = bank.create_customer('Anne', 'Smith')
a3 = bank.create_account(c2)
a4 = bank.create_account(c2, 'EUR')
print(bank)
