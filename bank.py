
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
    yearly_interest_rate = 0.02  # TODO - will be used to update the interest rate

    def __init__(self, customer, currency = 'USD'):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self.__balance = 0
        self.currency = currency

    def deposit(self, amount):
        # TODO - as part of the home assignment please extend this method
        """Add money to the account."""
        #value = self.__validate_amount(amount)
        if amount <= 0:
            #return False
            raise InvalidAmountException('Invalid amount: {}'.format(amount))
        self.__balance += amount
        return True

    def charge(self, amount):
        # TODO - as part of the home assignment please extend this method
        """Charge the account."""
        if self.__balance < amount:
            raise NotEnoughMoneyException('Not enough balance requested/available: {}/{}'.format(amount, self.__balance))
        self.__balance -= amount
        return True

        return self.__balance

    def __repr__(self):
        return f"A[{self.id}, {self.customer.last_name}, {self.__balance}]"


class Bank:
    def __init__(self, name):
        self.name = name
        self.acc_list = []
        self.cust_list = []

    def create_customer(self, first_name, last_name):
        customer = Customer(first_name, last_name)
        self.cust_list.append(customer)
        return customer

    def create_account(self, customer, currency = 'USD'):
        account = Account(customer, currency)
        self.acc_list.append(account)
        return account

    def transfer_money(self, from_account_id, to_account_id, amount):
        # TODO - as part of the home assignment please implement this method - as names suggest the input parameters are
        # ids of the accounts to transfer money from and to and amount to transfer. You may need a helper method to find
        # those accounts based on their ids.
        pass

    def run_daily_interest_updater(self):
        # TODO - as part of the home assignment please implement this method
        pass

    def __repr__(self):
        return f'Bank[{self.name},\n{self.cust_list}\n{self.acc_list}]'


class BankException(Exception):
    pass

class InvalidAmountException(BankException):
    pass

class NotEnoughMoneyException(BankException):
    pass