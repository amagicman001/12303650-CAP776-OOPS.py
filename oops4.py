class Loan:
    def __init__(self, principal, rate, years):
        self.principal = principal
        self.rate = rate
        self.years = years

class SimpleInterestLoan(Loan):
    def calculate_interest(self):
        interest = (self.principal * self.rate * self.years) / 100
        return interest

    def total_amount(self):
        return self.principal + self.calculate_interest()

class CompoundInterestLoan(Loan):
    def __init__(self, principal, rate, years, compounds_per_year=1):
        super().__init__(principal, rate, years)
        self.compounds_per_year = compounds_per_year

    def calculate_interest(self):
        amount = self.principal * (1 + self.rate / (100 * self.compounds_per_year)) ** (self.compounds_per_year * self.years)
        interest = amount - self.principal
        return interest

    def total_amount(self):
        return self.principal + self.calculate_interest()

si_loan = SimpleInterestLoan(10000, 5, 3)
si_interest = si_loan.calculate_interest()
si_total = si_loan.total_amount()
print(f"Simple Interest: {si_interest}")
print(f"Total Amount after SI: {si_total}")

ci_loan = CompoundInterestLoan(10000, 5, 3, 4)
ci_interest = ci_loan.calculate_interest()
ci_total = ci_loan.total_amount()
print(f"Compound Interest: {ci_interest}")
print(f"Total Amount after CI: {ci_total}")
