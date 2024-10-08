# Base class - Account
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self._account_number = account_number
        self._account_holder = account_holder 
        self._balance = balance 

    def deposit(self, amount):  
        self._balance += amount
        print(f"Deposited {amount}. New balance is: {self._balance}")

    def withdraw(self, amount):  
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is: {self._balance}")

    def get_balance(self):
        return self._balance

    def __del__(self): 
        print(f"Account {self._account_number} is closed.")

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self._interest_rate = interest_rate

    def apply_interest(self): 
        interest = self._balance * self._interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} applied at rate {self._interest_rate * 100}%")


class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):  # Overriding method (Run-time Polymorphism)
        if amount > self._balance + self._overdraft_limit:
            print("Overdraft limit exceeded")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is: {self._balance}")

# Polymorphism: both SavingsAccount and CurrentAccount can be treated as Account
def print_account_info(account):  # Run-time Polymorphism
    print(f"Account Holder: {account._account_holder}")
    print(f"Account Balance: {account.get_balance()}")

# Compile-time Polymorphism: Method Overloading (achieved using default arguments)
def create_account(account_type, account_number, account_holder, balance=0, interest_rate=None, overdraft_limit=None):
    if account_type == "Savings":
        return SavingsAccount(account_number, account_holder, balance, interest_rate)
    elif account_type == "Current":
        return CurrentAccount(account_number, account_holder, balance, overdraft_limit)
    else:
        print("Invalid account type")

# Abstraction: Clients of the bank only interact with the Account interface, unaware of the underlying implementation
savings = create_account("Savings", "SA123", "Alice", 1000, interest_rate=0.03)
current = create_account("Current", "CA456", "Bob", 500, overdraft_limit=1000)

savings.deposit(500)
savings.apply_interest()

current.withdraw(300)
current.withdraw(1500)

# Polymorphism
print_account_info(savings)
print_account_info(current)

