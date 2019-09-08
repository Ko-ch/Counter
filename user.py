class User:
    def __init__(self, name, age, country):
        # インスタンス変数
        self.name = name
        self.age = age
        self.country = country

    def display_profile(self):
        # display_profile()はUserクラスの、インスタンスメソッドです
        print(f'名前：{self.name} 国籍：{self.country} {self.age}歳')

    def dif_age(self):
        dif_age = 30 - int(self.age)
        if dif_age > 0:
            print(f'私は{self.name}より、' + str(abs(dif_age)) + '歳年上です。')
        if dif_age == 0:
            print(f'私と{self.name}は同い年です。')
        if dif_age < 0:
            print(f'私は{self.name}より、' + str(abs(dif_age)) + '歳年下です。')

    def change_nationality(self, country_name):
        self.country = country_name


if __name__ == '__main__':
    bob = User("Bob", 15, "USA")  # Userクラスのインスタンス化
    bob.display_profile()
    bob.dif_age()
    bob.change_nationality("China")
    bob.display_profile()

    tom = User("Tom", 57, "USA")
    tom.display_profile()
    tom.dif_age()
    tom.change_nationality("Italy")
    tom.display_profile()

    ken = User("Ken", 49, "JP")
    ken.display_profile()
    ken.dif_age()
    ken.change_nationality("Canada")
    ken.display_profile()
