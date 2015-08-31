__author__ = 'dick'
__email__ = 'ralbayaty@gmail.com'

import random
import time


def merge_sort(items):
    if len(items) == 1:
        return items
    m = round(len(items)/2)
    l = merge_sort(items[:m])
    r = merge_sort(items[m:])
    sorted_it = []

    while len(l) > 0 and len(r) > 0:
        # Checking the first value of each array, "pop" the lower value off the array and compare again
        if l[0] < r[0]:
            sorted_it.append(l[0])
            l = l[1:]
        else:
            sorted_it.append(r[0])
            r = r[1:]

    # Get the rest of the values from the arrays, if one array was larger than the other above
    if len(l) == 0:
        for val in r:
            sorted_it.append(val)
    if len(r) == 0:
        for val in l:
            sorted_it.append(val)
    return sorted_it

if __name__ == '__main__':
    # Generate a list of random integers
    random_items = [random.randint(-50, 100) for _ in range(32)]

    start = time.time()
    print('Before: ', random_items)
    sorted_items = merge_sort(random_items.copy())
    print('\nMy Merge Sort: \n   ', sorted_items)
    print("    It took: %.6f" % (time.time()-start))
