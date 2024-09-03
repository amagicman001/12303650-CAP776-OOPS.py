class ATM:
    def __init__(self, balance=0):
        self._balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is {self._balance}.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Your current balance is {self._balance}.")

atm = ATM()
atm.deposit(500)
atm.withdraw(200)
atm.check_balance()
atm.withdraw(400)
atm.deposit(300)
atm.check_balance()

