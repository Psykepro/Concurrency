'''Average runtime 7.39 seconds on my computer'''
import numpy as np
from timeit import default_timer as t

def prepare_data():
    np.random.RandomState(100)
    arr = np.random.randint(0, 10, size=[300000, 150])
    return arr.tolist()

def find_nums_within_range_for_current_row(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

if __name__ == "__main__":
    data = prepare_data()

    start = t()

    for row in data:
        find_nums_within_range_for_current_row(row, minimum=4, maximum=8)

    elapsed_time = t() - start
    print(f'Elapsed time: {elapsed_time:.2f} seconds')
