import datetime
import math

import threading
import multiprocessing


def main():
    cpu_counts = multiprocessing.cpu_count()
    print(f"Making main with {cpu_counts} core")
    start = datetime.datetime.now()
    threads = []
    for n in range(1, cpu_counts + 1):
        start_c = 50_000_00 * (n - 1) / cpu_counts
        end = 50_000_00 * n / cpu_counts
        print(f"core: {n}, start:, {start_c}, end: {end}")
        threads.append(
            threading.Thread(
                target=calculate, kwargs={"start": start_c, "end": end}, daemon=True
            )
        )
    [th.start() for th in threads]
    [th.join() for th in threads]
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
