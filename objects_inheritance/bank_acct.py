
class BankAccount:

    def __init__(self, name, amt):
        self.name = name
        self.amt = float(amt)

    def __str__(self):
        return 'Your account, {}, has {} dollars.'.format(self.name, self.amt)

t1 = BankAccount('Bob', 100.0)
print(t1)


