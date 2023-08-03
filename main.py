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


def hesap_islemleri(hesap):
    while True:
        print("\nHesap işlemleri:")
        print("1. Para yatırma")
        print("2. Para çekme")
        print("3. Bakiye sorgulama")
        print("0. Çıkış yap")
        secim = int(input("Yapmak istediğiniz işlemi seçin (0-3): "))

        if secim == 0:
            break
        elif secim == 1:
            yatirilan_miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
            hesap.deposit(yatirilan_miktar)
        elif secim == 2:
            cekilen_miktar = float(input("Çekmek istediğiniz miktarı girin: "))
            hesap.withdraw(cekilen_miktar)
        elif secim == 3:
            print("Güncel bakiye:", hesap.getbalance())
        else:
            print("Geçersiz seçim! Lütfen geçerli bir işlem seçin.")


def main():
    while True:
        hesaplar = {}
        ad = input("Hesap sahibinin adını girin (Çıkış yapmak için 'q' girin): ").strip()
        if ad.lower() == 'q':
            print("Çıkış yapılıyor...")
            break

        hesap = BankAccount(ad)
        hesaplar[ad] = hesap
        hesap_islemleri(hesaplar[ad])

        for ad, hesap in hesaplar.items():
            print(f"\n{ad} hesabının son bakiyesi: {hesap.getbalance():.2f} TL")


if __name__ == "__main__":
    main()
