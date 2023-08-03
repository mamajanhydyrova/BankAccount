class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getbalance(self):
        return self.balance

    def deposit(self, amout):
        self.balance += amout
        return self.balance

    def withdraw(self, amout):
        self.balance -= amout
        return self.balance


hesap = BankAccount("Mamajan")
hesap.deposit(150)
hesap.withdraw(60)

print(hesap.getbalance())
