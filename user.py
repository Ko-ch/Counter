class User:
    def __init__(self, name, age, country):
        # インスタンス変数
        self.name = name
        self.age = age
        self.country = country


if __name__ == '__main__':
    bob = User("Bob", 15, "USA")  # Userクラスのインスタンス化
    print(bob)  # <__main__.User object at 0x00000266C47C5088>
    print(bob.name)  # Bob
    print(bob.age)  # 15
    print(bob.country)  # USA

    tom = User("Tom", 57, "USA")
    print(tom)
    print(tom.name)
    print(tom.age)
    print(tom.country)

    ken = User("Ken", 49, "JP")
    print(ken)
    print(ken.name)
    print(ken.age)
    print(ken.country)
