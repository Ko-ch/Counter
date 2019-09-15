class Counter_1:
    def __init__(self, value):
        self.value = value

    def increase(self):
        if self.value <= 0:
            self.value += 5
            return self
        if self.value > 14:
            self.value += 3
            return self
        self.value += 1
        return self

    def decrease(self):
        self.value -= 1
        return self


if __name__ == "__main__":
    counter_1 = Counter_1(15)
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1 = Counter_1(-5)
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1 = Counter_1(0)
    print(counter_1.value)

    counter_1.decrease()
    print(counter_1.value)

    counter_1.decrease()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)
