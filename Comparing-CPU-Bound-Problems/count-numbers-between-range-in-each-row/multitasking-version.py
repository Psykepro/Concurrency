'''Average runtime 19.08 seconds on my computer'''
import asyncio
import numpy as np
from timeit import default_timer as t

def prepare_data():
    np.random.RandomState(100)
    arr = np.random.randint(0, 10, size=[300000, 150])
    return arr.tolist()

async def find_nums_within_range_for_current_row(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

async def find_all_nums_within_range(data):
    futures = []
    for row in data:
        futures.append(find_nums_within_range_for_current_row(row, 4, 8))
    await asyncio.gather(*futures)


if __name__ == "__main__":
    data = prepare_data()

    start = t()

    asyncio.run(find_all_nums_within_range(data))
    
    elapsed_time = t() - start
    print(f'Elapsed time: {elapsed_time:.2f} seconds')