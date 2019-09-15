class Counter_01:
    def __init__(self, value):
        self.value = value

    def increase_01(self):
        self.value += 1

    def increase_02(self):
        self.value += 3


if __name__ == "__main__":
    counter_01 = Counter_01(0)
    print(counter_01.value)

    counter_01.increase_01()
    print(counter_01.value)

    counter_01.increase_01()
    print(counter_01.value)

    counter_01 = Counter_01(15)
    print(counter_01.value)

    counter_01.increase_02()
    print(counter_01.value)

    counter_01.increase_02()
    print(counter_01.value)
