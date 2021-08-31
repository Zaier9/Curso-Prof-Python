from typing import Generic, TypeVar

T = TypeVar('T')

def make_divisor_by(n: int) -> Generic[T]:
    def numerator(x: int) -> float:
        assert n != 0, "You can't divide by zero."
        return x/n
    return numerator

def main():
    division_by_2 = make_divisor_by(2)
    print(division_by_2(10))

    division_by_3 = make_divisor_by(3)
    print(division_by_3(90))

if __name__ == '__main__':
    main()
