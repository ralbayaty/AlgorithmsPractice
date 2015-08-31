__author__ = 'dick'
__email__ = 'ralbayaty@gmail.com'


import time


def fib(n):
    """
    Generate the n th Fibonacci number using recursive function calls.
    :param n: the desired number in the sequence
    :return: the n th number in the sequence
    """
    if n < 0:
        n = 0
    return n if n < 2 else fib2(n-1) + fib2(n-2)


def fib2(n):
    """
    Generate the n th Fibonacci number using recursive function calls a different way.
    :param n: the desired number in the sequence
    :return: the n th number in the sequence
    """
    if n < 1:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


def fib_lists(n):
    """
    Generate the n th Fibonacci number using lists. This method ends up running faster for larger n.
    :param n: the desired number in the sequence
    :return: the n th number in the sequence
    """
    fib_nums = [0, 1]
    for i in range(2, n+1):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
    return fib_nums[n]


if __name__ == "__main__":

    # Show the amount of time it takes each method in seconds.
    # The fib() and fib2() should roughly be the same.
    for i in range(1, 40, 1):
        start1 = time.time()
        fib_lists(i)
        end1 = time.time()
        fib(i)
        end2 = time.time()
        fib2(i)
        end3 = time.time()
        print(i, end1-start1, end2-end1, end3-end2)
