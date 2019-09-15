class Counter:
    def __init__(self, value, num):
        self.value = value
        self.num = num

    def increase(self):
        self.value += self.num


if __name__ == "__main__":
    counter_1 = Counter(0, 1)
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)
