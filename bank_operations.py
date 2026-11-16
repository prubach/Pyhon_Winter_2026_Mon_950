#from bank import Bank, Customer, Account
from bank import *


try:
    bank = Bank('SGH Bank')
    c1 = bank.create_customer('John', 'Brown')
    a1 = bank.create_account(c1)
    a1.deposit(100)
    a2 = bank.create_account(c1, 'EUR')
    c2 = bank.create_customer('Anne', 'Smith')
    a3 = bank.create_account(c2)
    a4 = bank.create_account(c2, 'EUR')
    #res = a4.deposit(-300)
    #if res:
    #    print("Deposit successful")
    #else:
    #    print("Deposit failed")
    print(bank)
    print('--- operations ----')
    import sys
    #sys.exit(-100)
    a1.charge(150)
    #a4.charge('100')
    print(bank)
except BankException as e:
    print(e)

#2>&1


# TODO
# Implement deposit and charge methods to allow manipulating the balance of each account. Take into account various scenarios...