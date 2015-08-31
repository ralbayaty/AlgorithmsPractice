__author__ = 'dick'
__email__ = 'ralbayaty@gmail.com'


fcache = {}


def fib(n):
    """
    Generate the n th Fibonacci number using lists, fetching from cache if already created.
    :param n: the desired number in the sequence
    :return: the n th number in the sequence
    """
    if n in fcache:
        print("Fetched it!")
        return fcache[n]
    else:
        fcache[n] = n if n < 2 else fib(n-1) + fib(n-2)
        print("Storing it!")
        return fcache[n]


if __name__ == "__main__":
    # Create a range of Fibonacci numbers
    for i in range(3, 10):
        print(fib(i))

    # See that the numbers that were already created were
    # pulled from the cache instead of being recreated.
    # New numbers end up fetching the last 2 stored ones.
    for i in range(15):
        print(fib(i))
