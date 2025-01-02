from typing import Generator


def fib() -> Generator[int, None, None]:
    value: int = 0
    next_value: int = 1
    while True:
        value, next_value = next_value, value + next_value
        yield value


if __name__ == "__main__":
    for n in fib():
        print(n, end=", ")
        if n > 100:
            break

    print("\nReady")
