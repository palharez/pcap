import time
import colorama

from threading import Thread
from queue import Queue


def generate(queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f"Data {i} generated", flush=True)
        time.sleep(2)
        queue.put(i)


def consumer(queue):
    while queue.qsize() > 0:
        value = queue.get()
        print(colorama.Fore.RED + f"Data {value * 2} processed", flush=True)
        time.sleep(1)
        queue.task_done()


if __name__ == "__main__":
    print(colorama.Fore.BLUE + "System Started", flush=True)
    queue = Queue()
    first_thread = Thread(target=generate, args=(queue,))
    second_thread = Thread(target=consumer, args=(queue,))
    first_thread.start()
    first_thread.join()
    second_thread.start()
    second_thread.join()
