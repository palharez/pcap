import multiprocessing

def calculate(number):
    return number ** 2

def main():
	pool_size = multiprocessing.cpu_count() * 2

	print(f"Pool size: {pool_size}")

	pool = multiprocessing.Pool(processes=pool_size)

	inputs = list(range(7))
	outs = pool.map(calculate, inputs)
	print(f"Outs: {outs}")
	pool.close()
	pool.join()

if __name__ == "__main__":
    main()
