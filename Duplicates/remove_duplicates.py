__author__ = 'dick'
__email__ = 'ralbayaty@gmail.com'

import random
import heapq
import time


def make_duplicates_file(file_name, num_items=10000):
    """
    Creates a text files with random ints
    :param file_name: the desired name of the output file
    :param num_items: the number of ints you want in the file
    :return: nothing
    """
    with open(file_name, 'w') as f:
        for i in range(num_items):
            f.write(str(random.randint(-1000, 1000)) + "\n")


def make_chunks(f, chunk_size=1):
    """
    A function to read chucks of lines from a file
    :param f: the text file object
    :return: a list containing the chucks of lines from the file
    """
    chunk_list = []
    for i in range(chunk_size):
        item = f.readline()
        if item is not '':
            chunk_list.append(int(item))
    return chunk_list


def remove_multiples(f):
    """
    A generator that returns values of unique consecutive items in the file
    :param f: the text file object
    :return: yields the value
    """
    a = f.readline()
    while True:
        temp = f.readline()
        if not temp:
            yield a
            break
        if temp == a:
            temp = f.readline()
        else:
            yield a
            a = temp


if __name__ == "__main__":
    start_time = time.time()
    # Generate the unsorted random integer file
    make_duplicates_file("files/duplicate_list.txt", 10**4)

    # Make sure the output file is fresh and empty
    with open("files/sorted_list.txt", "w") as file_name:
        pass

    with open("files/duplicate_list.txt", "r") as big_file:
        iters = []
        while True:
            # break the file into manageable "chunks"
            b = make_chunks(big_file, 10000)

            # When there is no more data to ingest, leave this loop
            if not b:
                break

            # Pass a generator for the sorted values
            iters.append(x for x in sorted(b))

    b = []
    item_num = 0
    for x in heapq.merge(*iters):
        b.append(str(x)+"\n")
        # Write b to file in chucks to avoid data IO issues
        if len(b) >= 1000:
            with open("files/sorted_list.txt", "a") as file_name:
                file_name.writelines(b)
            del b
            b = []
        item_num += 1

    # Write any remaining values in b to file (it might not have passed the write buffer size on last iteration)
    if b:
        with open("files/sorted_list.txt", "a") as file_name:
                file_name.writelines(b)

    # Remove duplicates
    with open("files/sorted_list.txt", "r") as file_name_sorted:
        with open("files/unduplicated_sorted_list.txt", "w") as file_name:
            file_name.writelines(remove_multiples(file_name_sorted))

    print("There were", item_num, "total items in the big file.")
    print("It took", time.time()-start_time, "seconds to process.")