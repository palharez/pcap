import multiprocessing


def ping(conn):
    conn.send('Ping')


def pong(conn):
    msg = conn.recv()
    print(f'{msg}-Pong')


def main():
    conn_1, conn_2 = multiprocessing.Pipe(True)
    p1 = multiprocessing.Process(target=ping, args=(conn_1,))
    p2 = multiprocessing.Process(target=pong, args=(conn_2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
