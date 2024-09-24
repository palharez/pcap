import datetime
import math


def main():
    start = datetime.datetime.now()
    calculate(end=50_000_00)
    finish = datetime.datetime.now() - start
    print(f"Finshed at {finish.total_seconds():.2f} secs.")


def calculate(end, start=1):
    current = start
    factor = 1000 * 1000
    while current < end:
        current += 1
        math.sqrt((current - factor) * (current - factor))


if __name__ == "__main__":
    main() 
