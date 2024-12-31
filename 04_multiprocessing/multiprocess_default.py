import datetime
import math

import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor as Executor


def main():
    cpu_counts = multiprocessing.cpu_count()
    print(f"Making main with {cpu_counts} core")
    start = datetime.datetime.now()

    with Executor(max_workers=cpu_counts) as executor:
        for n in range(1, cpu_counts + 1):
            start_c = 50_000_00 * (n - 1) / cpu_counts
            end = 50_000_00 * n / cpu_counts
            print(f"core: {n}, start:, {start_c}, end: {end}")
            executor.submit(calculate, start=start_c, end=end)
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
