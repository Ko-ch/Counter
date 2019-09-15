class Counter:
    def __init__(self, value):
        self.value = value

    def increase(self):
        self.value += 1
        return self

    def decrease(self):
        self.value -= 1
        return self


if __name__ == "__main__":
    counter_1 = Counter(15)
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1 = Counter(0)
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1 = Counter(0)
    print(counter_1.value)

    counter_1.decrease()
    print(counter_1.value)

    counter_1.decrease()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)
