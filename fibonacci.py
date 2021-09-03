import time


class FiboIter():

    def __init__(self, max:int):
        self.max = max

    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.counter = 0
        return self


    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.num1
        elif self.counter == 1:
            self.counter += 1
            return self.num2
        else:
            if self.counter <= self.max:
                self.aux = self.num1 + self.num2
                self.num1, self.num2 = self.num2, self.aux
                self.counter += 1
                return self.aux
            else:
                raise StopIteration


if __name__ == '__main__':
    fibonacci = FiboIter

    for element in fibonacci(50):
        print(element)
        time.sleep(0.5)
