import threading
import time


def count(animal, number):
    for n in range(number):
        print(f"{n+1} {animal}")
        time.sleep(1)


def main():
    th = threading.Thread(target=count, args=("elephant", 10))
    th.start()  # Adds thread to pool
    print("We can do another things while execute the thread")
    th.join()  # Await to finish the thread
    print("Finishing")


if __name__ == "__main__":
    main()
