
class Customer:
    last_id = 0
    def __init__(self, first_name, last_name):
        Customer.last_id += 1
        self.id = Customer.last_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"C[{self.id}, {self.last_name}]"

class Account:
    last_id = 1000

    def __init__(self, customer, currency = 'USD'):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self.__balance = 0
        self.currency = currency

    def __repr__(self):
        return f"A[{self.id}, {self.customer.last_name}]"


class Bank:
    def __init__(self, name):
        self.name = name
        self.acc_list = []
        self.cust_list = []

    def create_customer(self, first_name, last_name):
        customer = Customer(first_name, last_name)
        self.cust_list.append(customer)
        return customer

    def create_account(self, customer, currency):
        account = Account(customer, currency)
        self.acc_list.append(account)
        return account

    def __repr__(self):
        return f'Bank[{self.name},\n{self.cust_list}\n{self.acc_list}]'


