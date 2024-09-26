import threading
import time


def count(animal, number):
    for n in range(number):
        print(f"{n+1} {animal}")
        time.sleep(1)


def main():
    threads = [
        threading.Thread(target=count, args=("tiger", 5)),
        threading.Thread(target=count, args=("monkey", 6)),
        threading.Thread(target=count, args=("shark", 8)),
        threading.Thread(target=count, args=("elephant", 10)),
    ]
    [th.start() for th in threads]
    print("We can do another things while execute the thread")
    [th.join() for th in threads]
    print("Finishing")


if __name__ == "__main__":
    main()
