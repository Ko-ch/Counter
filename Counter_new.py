class Counter_01:
    def __init__(self, value):
        self.value = value

    def increase(self):
        self.value += 1


if __name__ == "__main__":
    counter_01 = Counter_01(0)
    print(counter_01.value)

    counter_01.increase()
    print(counter_01.value)

    counter_01.increase()
    print(counter_01.value)
