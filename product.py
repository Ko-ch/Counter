# productクラスのインスタンス化
class Product:
    def __init__(self, name, amount):
        self.name = name  # nameというインスタンス変数
        self.amount = amount

    def discount(self, price):
        self.amount -= price

if __name__ == "__main__":
    p1 = Product("iPhone", 100000)  # Productクラスのインスタント化
    print(p1)
    print(p1.name)  # iPhone
    p1.discount(5000)
    print(p1.amount)  # 100,000

    p2 = Product("MacBookAir", 150000)
    print(p2)
    print(p2.name)
    p2.discount(10000)
    print(p2.amount)

    p3 = Product("AppleWatch", 50000)
    print(p3)
    print(p3.name)
    p3.discount(2500)
    print(p3.amount)
