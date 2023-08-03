class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getbalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount:.2f} TL yatırıldı. Yeni bakiye: {self.balance:.2f} TL")
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount:.2f} TL çekildi. Yeni bakiye: {self.balance:.2f} TL")
            return self.balance
        else:
            print("Yetersiz bakiye.")
            return self.balance


ad = input("Hesap sahibinin adını girin: ")
hesap = BankAccount(ad)

yatirilan_miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
hesap.deposit(yatirilan_miktar)

cekilen_miktar = float(input("Çekmek istediğiniz miktarı girin: "))
hesap.withdraw(cekilen_miktar)

print("Son bakiye:", hesap.getbalance())
