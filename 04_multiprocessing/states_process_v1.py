import multiprocessing
import time


def func_1(val, stat):
	if stat:
		res = val + 10
		stat = False
	else:
		res = val + 20
		val = 200
		stat = True

	print(f'The function 1 result is {res}')
	time.sleep(0.002)


def func_2(val, stat):
	if stat:
		res = val + 30
		stat = False
	else:
		res = val + 40
		val = 400
		stat = True

	print(f'The function 2 result is {res}')
	time.sleep(0.002)


def main():
	val = 100
	state = False

	p1 = multiprocessing.Process(target=func_1, args=(val, state))
	p2 = multiprocessing.Process(target=func_2, args=(val, state))

	p1.start()
	p2.start()

	p1.join()
	p2.join()


if __name__ == '__main__':
    main()
