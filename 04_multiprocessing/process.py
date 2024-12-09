import multiprocessing

print(f"Starting with process: {multiprocessing.current_process().name}")


def do_something(value):
    print(f"Do something with {value}")


def main():
    pc = multiprocessing.Process(
        target=do_something,
        args=["Birds"],
        name="Geek Proccess"
    )

    print(f"Starting the process {pc.name}")

    pc.start()
    pc.join()

main()
