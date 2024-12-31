import time

# from concurrent.futures.thread import ThreadPoolExecutor as Executer
from concurrent.futures.process import ProcessPoolExecutor as Executer


def process():
    print("|", end="", flush=True)
    for _ in range(1, 11):
        print("#", end="", flush=True)
        time.sleep(0.1)
    print("|", end="", flush=True)
    return 42


if __name__ == "__main__":
    with Executer() as executer:
        future = executer.submit(process)
    print(f"The return of executor is {future.result()}")
