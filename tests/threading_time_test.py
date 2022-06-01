import time
from prtpy.packing.bin_completion import bin_completion
from prtpy.bins import BinsKeepingContents
import random
import matplotlib.pyplot as plt

def create_input_file():

    inputs = []
    size = 15

    for _ in range(9):
        items = []
        for i in range(size):
            items.append(random.randint(1, 100))

        inputs.append(sorted(items, reverse=True))
        size += 2

    with open("input.txt", "w") as input_file:
        for res in inputs:
            for item in res:
                input_file.write(f"{item} ")

            input_file.write('\n')

if __name__ == "__main__":
    # create_input_file()
    inputs = []
    results = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            items = [int(x) for x in line.split()]
            inputs.append(items)
            print(f"Working on {items}")
            start = time.perf_counter()
            bin_completion(BinsKeepingContents(), 100, items)
            finish = time.perf_counter()

            t_result = round(finish - start, 2)
            print(f"Finished {len(items)} items in {t_result} seconds.")
            results.append(t_result)

    x = [len(input) for input in inputs]
    plt.plot(x, results)
    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")
    plt.show()
    print(f"Input Sizes = {x}")
    print(f"Results = {results}")