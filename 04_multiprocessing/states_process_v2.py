import multiprocessing
import time
import ctypes


def func_1(val, stat):
	if stat.value:
		res = val.value + 10
		stat.value = False
	else:
		res = val.value + 20
		val.value = 200
		stat.value = True

	print(f'The function 1 result is {res}')
	time.sleep(0.002)


def func_2(val, stat):
	if stat.value:
		res = val.value + 30
		stat.value = False
	else:
		res = val.value + 40
		val.value = 400
		stat.value = True

	print(f'The function 2 result is {res}')
	time.sleep(0.002)


def main():
	val = multiprocessing.Value('i', 100)
	state = multiprocessing.Value(ctypes.c_bool, False)

	p1 = multiprocessing.Process(target=func_1, args=(val, state))
	p2 = multiprocessing.Process(target=func_2, args=(val, state))

	p1.start()
	p2.start()

	p1.join()
	p2.join()


if __name__ == '__main__':
    main()
