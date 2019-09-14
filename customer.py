class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def full_name_JPver(self):
        return f"{self.family_name} {self.first_name}"

    def display_profile(self):
        print(f"Name: {self.full_name()}, Age: {str(self.age)}")

    def info_csv(self):
        return f"{self.full_name()},{self.age}"


if __name__ == "__main__":
    tom = Customer("Tom", "Ford", 57)
    ken = Customer("Ken", "Yokoyama", 49)
    koch = Customer("Koichiro", "Takagi", 30)

    tom.display_profile()  # "Name: Tom Ford, Age: 57"と出力する
    ken.display_profile()
    koch.display_profile()

    print(ken.full_name_JPver())
    print(koch.full_name_JPver())
