'''Average runtime 17.83 seconds on my computer'''

import concurrent.futures
from timeit import default_timer as timer


def sum_squares_in_range(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(sum_squares_in_range, numbers)
           

if __name__ == '__main__':
    numbers = [6_000_000] * 20
    start_time = timer()
    find_sums(numbers)
    elapsed = timer() - start_time
    print(f"Execution time: {elapsed:.2f} seconds")
