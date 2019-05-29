'''Average runtime 18.04 seconds on my computer'''

from timeit import default_timer as timer


def sum_squares_in_range(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        sum_squares_in_range(number)


if __name__ == "__main__":
    numbers = [6_000_000] * 20
    start_time = timer()
    find_sums(numbers)
    elapsed = timer() - start_time
    print(f"Execution time: {elapsed:.2f} seconds")