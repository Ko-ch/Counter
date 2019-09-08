# productクラスのインスタンス化
class Product:
    def __init__(self, name, price):
        self.name = name  # nameというインスタンス変数
        self.price = price


if __name__ == "__main__":
    p1 = Product("iPhone", 100000)  # Productクラスのインスタント化
    print(p1)
    print(p1.name)  # iPhone
    print(p1.price)  # 100,000

    p2 = Product("MacBookAir", 150000)
    print(p2)
    print(p2.name)
    print(p2.price)

    p3 = Product("AppleWatch", 50000)
    print(p3)
    print(p3.name)
    print(p3.price)
